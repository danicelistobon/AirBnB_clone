#!/usr/bin/python3
"""Module Unit Tests
"""


import unittest
from models.amenity import Amenity
import pep8


class Test_amenity(unittest.TestCase):
    """Amenity Unit Tests
    """

    def test_pep8_amenity(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_pep8_testamenity(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """Test docstring
        """
        self.assertTrue(len(Amenity.__doc__) > 1)

    def test_inst(self):
        """Test is instance
        """
        a = Amenity()
        self.assertIsInstance(a, Amenity)

    def test_basic(self):
        """Test for BaseModel
        """
        a = Amenity()
        a.name = "Holberton"
        a.number = 89
        self.assertEqual([a.name, a.number], ["Holberton", 89])
