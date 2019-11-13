#!/usr/bin/python3
"""Module Unit Tests
"""


import unittest
from models.state import State
import pep8


class Test_state(unittest.TestCase):
    """User Unit Tests
    """

    def test_pep8_state(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['models/state.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_pep8_teststate(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """Test docstring
        """
        self.assertTrue(len(State.__doc__) > 1)

    def test_inst(self):
        """Test is instance
        """
        s = State()
        self.assertIsInstance(s, State)

    def test_basic(self):
        """Test for BaseModel
        """
        s = State()
        s.name = "Holberton"
        s.number = 89
        self.assertEqual([s.name, s.number], ["Holberton", 89])
