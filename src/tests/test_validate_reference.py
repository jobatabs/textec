import unittest
from util import validate_reference, UserInputError


class TestValidateReference(unittest.TestCase):
    def test_valid_pp_and_year(self):
        raised = False
        try:
            validate_reference("Mikko Mallikainen",
                               "Artikkeli", "Lehti", 2001, "213")
        except UserInputError:
            raised = True
        self.assertFalse(raised)

    def test_valid_pp_range(self):
        raised = False
        try:
            validate_reference("Mikko Mallikainen",
                               "Artikkeli", "Lehti", 2001, "213-250")
        except UserInputError:
            raised = True
        self.assertFalse(raised)

    def test_invalid_pp(self):
        self.assertRaises(UserInputError, validate_reference,
                          "Mikko Mallikainen", "Artikkeli", "Lehti", 2001, "kaksi")
    
    def test_pp_too_long(self):
        self.assertRaises(UserInputError, validate_reference, "Mikko Mallikainen", "Artikkeli", "Lehti",
                          2001, "aivanliianpitkä, siis naurettavan pitkä, aivan todella pitkä merkkijono")

    def test_invalid_year(self):
        self.assertRaises(UserInputError, validate_reference, "Mikko Mallikainen", "Artikkeli", "Lehti",
                          "kaksituhattayksi", "213")
