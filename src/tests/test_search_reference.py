import unittest
from app import app
from db_helper import reset_db, setup_db_tests


class TestSearchRoutes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.app_context = app.app_context()
        cls.app_context.push()

        setup_db_tests()

    @classmethod
    def tearDownClass(cls):
        cls.app_context.pop()

    def setUp(self):
        reset_db()
        self.client = app.test_client()

        self.client.post(
            "/create",
            data={
                "type": "article",
                "author": "Author A",
                "title": "Title A",
                "year": "2021",
                "journal": "Journal A",
            },
            follow_redirects=True,
        )

        self.client.post(
            "/create",
            data={
                "type": "book",
                "author": "Author B",
                "title": "Title B",
                "year": "2019",
                "publisher": "Publisher B",
            },
            follow_redirects=True,
        )

    def test_search_with_results(self):
        response = self.client.get("/result?query=Author A")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Title A", response.data)
        self.assertIn(b"Author A", response.data)
        self.assertNotIn(b"Title B", response.data)
        self.assertNotIn(b"Author B", response.data)

    def test_search_with_no_results(self):
        response = self.client.get("/result?query=Nonexistent")
        self.assertEqual(response.status_code, 200)

    def test_search_with_empty_query(self):
        response = self.client.get("/result?query=")
        self.assertEqual(response.status_code, 302)

    def test_search_case_insensitivity(self):
        response = self.client.get("/result?query=author a")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Title A", response.data)
        self.assertIn(b"Author A", response.data)

    def test_search_partial_match(self):
        response = self.client.get("/result?query=Author")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Title A", response.data)
        self.assertIn(b"Title B", response.data)
        self.assertIn(b"Author A", response.data)
        self.assertIn(b"Author B", response.data)


if __name__ == "__main__":
    unittest.main()
