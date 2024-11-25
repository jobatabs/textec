import unittest
from app import app
from db_helper import reset_db, setup_db
import os


class TestReferenceRoutes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.app_context = app.app_context()
        cls.app_context.push()

        setup_db()

    @classmethod
    def tearDownClass(cls):
        cls.app_context.pop()
        if os.path.exists("references.bib"):
            os.remove("references.bib")

    def setUp(self):
        reset_db()
        self.client = app.test_client()

        self.client.post(
            "/create",
            data={
                "author": "Author A",
                "title": "Title A",
                "journal": "Journal A",
                "year": "2021"
            },
            follow_redirects=True
        )

    def test_generate_bibfile(self):
        response = self.client.get(
            "/export_bibtex_file", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        with open("references.bib", "r") as f:
            generated_bib = f.read()

        expected_bib_file = (
            '@Article{Tit2021,\n'
            '  author   = "Author A",\n'
            '  title    = "Title A",\n'
            '  journal  = "Journal A",\n'
            '  year     = 2021\n'
            '}\n\n'
        )
        self.assertEqual(generated_bib, expected_bib_file)


if __name__ == "__main__":
    unittest.main()
