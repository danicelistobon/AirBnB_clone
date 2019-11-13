#!/usr/bin/python3
"""Module Unit Tests
"""


import unittest
from models.place import Place
import pep8


class Test_place(unittest.TestCase):
    """User Unit Tests
    """

    def test_pep8_place(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['models/place.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_pep8_testplace(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """Test docstring
        """
        self.assertTrue(len(Place.__doc__) > 1)

    def test_inst(self):
        """Test is instance
        """
        p = Place()
        self.assertIsInstance(p, Place)

    def test_basic(self):
        """Test for BaseModel
        """
        p = Place()
        p.name = "Holberton"
        p.number = 89
        self.assertEqual([p.name, p.number], ["Holberton", 89])
