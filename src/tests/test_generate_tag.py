import unittest
from bib_generator import generate_tag
from entities.reference import Reference


class TestGenerateTag(unittest.TestCase):
    def setUp(self):
        self.ref = Reference(_id=0, category="Book", author="Turing, A.",
                             year="1937", title="On Computable Numbers, with an Application to the Entscheidungsproblem")
        self.shortref = Reference(
            _id=1, category="Article", author="A", title="B", year="3")
        self.spaceref = Reference(
            _id=2, author="    B   ", year="1997", title="Title", category="misc")

    def test_tag_generation(self):
        self.assertEqual(generate_tag(self.ref, set()), "Tur1937")

    def test_colliding_tags(self):
        tags = set()
        tags.add(generate_tag(self.ref, set()))
        self.assertEqual(generate_tag(self.ref, tags), "Tur1937-2")

    def test_short_tag(self):
        self.assertEqual(generate_tag(self.shortref, set()), "A3")

    def test_author_spaces(self):
        self.assertEqual(generate_tag(self.spaceref, set()), "B1997")
