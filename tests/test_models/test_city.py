#!/usr/bin/python3
"""Module Unit Tests
"""


import unittest
from models.city import City
import pep8


class Test_city(unittest.TestCase):
    """City Unit Tests
    """

    def test_pep8_city(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['models/city.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_pep8_testcity(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """Test docstring
        """
        self.assertTrue(len(City.__doc__) > 1)

    def test_inst(self):
        """Test is instance
        """
        c = City()
        self.assertIsInstance(c, City)

    def test_basic(self):
        """Test for BaseModel
        """
        c = City()
        c.name = "Holberton"
        c.number = 89
        self.assertEqual([c.name, c.number], ["Holberton", 89])
