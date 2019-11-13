#!/usr/bin/python3
"""Module Unit Tests
"""


import unittest
from models.engine.file_storage import FileStorage
import pep8


class Test_file_storage(unittest.TestCase):
    """BaseModel Unit Tests
    """

    def test_pep8(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_pep8_testfile_storage(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(
                        ['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """Test docstring
        """
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_inst(self):
        """Test is instance
        """
        f = FileStorage()
        self.assertIsInstance(f, FileStorage)
