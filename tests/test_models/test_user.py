#!/usr/bin/python3
"""Module Unit Tests
"""


import unittest
from models.user import User
import pep8


class Test_user(unittest.TestCase):
    """User Unit Tests
    """

    def test_pep8_user(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['models/user.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_pep8_testuser(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """Test docstring
        """
        self.assertTrue(len(User.__doc__) > 1)

    def test_inst(self):
        """Test is instance
        """
        u = User()
        self.assertIsInstance(u, User)

    def test_basic(self):
        """Test for BaseModel
        """
        u = User()
        u.name = "Holberton"
        u.number = 89
        self.assertEqual([u.name, u.number], ["Holberton", 89])
