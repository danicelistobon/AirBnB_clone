#!/usr/bin/python3
"""Module Unit Tests
"""


import unittest
from models.base_model import BaseModel
import pep8
import uuid
from models import storage


class Test_base_model(unittest.TestCase):
    """BaseModel Unit Tests
    """

    def test_pep8(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_pep8_testbase(self):
        """Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(r.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """Test docstring
        """
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_inst(self):
        """Test is instance
        """
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_basic(self):
        """Test for BaseModel
        """
        base = BaseModel()
        base.name = "Holberton"
        base.number = 89
        self.assertEqual([base.name, base.number], ["Holberton", 89])

    def test_init(self):
        """Test __init__
        """
        base = BaseModel()
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

    def test_id(self):
        """Test id
        """
        base0 = BaseModel()
        base1 = BaseModel()
        self.assertEqual(uuid.UUID(base0.id).version, 4)
        self.assertFalse(base0.id == base1.id)

    def test_str(self):
        """Test __str__
        """
        base = BaseModel()
        printbase = base.__str__()
        self.assertEqual(printbase,
                         "[BaseModel] ({}) {}".format(base.id, base.__dict__))

    def test_save(self):
        """Test save
        """
        base = BaseModel()
        base.save()
        key = "BaseModel.{}".format(base.id)
        comp = storage._FileStorage__objects[key]
        self.assertEqual(base.id, comp.id)
