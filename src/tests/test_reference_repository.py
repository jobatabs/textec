import unittest
from app import app
from db_helper import reset_db, setup_db


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

    def setUp(self):
        reset_db()
        self.client = app.test_client()

    def test_create_reference_successful(self):
        response = self.client.post(
            "/create",
            data={
                "author": "Author A",
                "title": "Title A",
                "journal": "Journal A",
                "year": "2021"
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Successfully added reference Title A.", response.data)

        response = self.client.get("/")
        self.assertIn(b"Author A", response.data)
        self.assertIn(b"Title A", response.data)
        self.assertIn(b"Journal A", response.data)
        self.assertIn(b"2021", response.data)

    def test_create_reference_with_pp_successful(self):
        response = self.client.post(
            "/create",
            data={
                "author": "Author A",
                "title": "Title A",
                "journal": "Journal A",
                "year": "2021",
                "pp": "213-250"
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Successfully added reference Title A.", response.data)

        response = self.client.get("/")
        self.assertIn(b"Author A", response.data)
        self.assertIn(b"Title A", response.data)
        self.assertIn(b"Journal A", response.data)
        self.assertIn(b"2021", response.data)
        self.assertIn(b"(pp. 213-250)", response.data)

    def test_create_reference_invalid_year(self):
        response = self.client.post(
            "/create",
            data={
                "author": "Author A",
                "title": "Title A",
                "journal": "Journal A",
                "year": "not_a_year"
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Adding was unsuccessful. Invalid year.", response.data)

        response = self.client.get("/")
        self.assertNotIn(b"Author A", response.data)

    def test_create_reference_invalid_pp(self):
        response = self.client.post(
            "/create",
            data={
                "author": "Author A",
                "title": "Title A",
                "journal": "Journal A",
                "year": "2021",
                "pp": "kaksisataa"
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Adding was unsuccessful. Invalid pages pertinent", response.data)

        response = self.client.get("/")
        self.assertNotIn(b"Author A", response.data)

    def test_create_reference_negative_year(self):
        response = self.client.post(
            "/create",
            data={
                "author": "Author A",
                "title": "Title A",
                "journal": "Journal A",
                "year": "-1"
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Adding was unsuccessful. Invalid year.", response.data)

        response = self.client.get("/")
        self.assertNotIn(b"Author A", response.data)


if __name__ == "__main__":
    unittest.main()
