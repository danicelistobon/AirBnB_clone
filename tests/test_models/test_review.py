#!/usr/bin/python3
"""Module Unit Tests
"""


import unittest
from models.review import Review
import pep8


class Test_review(unittest.TestCase):
    """User Unit Tests
    """

    def test_pep8_review(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['models/review.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_pep8_testreview(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """Test docstring
        """
        self.assertTrue(len(Review.__doc__) > 1)

    def test_inst(self):
        """Test is instance
        """
        r = Review()
        self.assertIsInstance(r, Review)

    def test_basic(self):
        """Test for BaseModel
        """
        r = Review()
        r.name = "Holberton"
        r.number = 89
        self.assertEqual([r.name, r.number], ["Holberton", 89])
