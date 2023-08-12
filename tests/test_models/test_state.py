#!/usr/bin/python3
"""Define the unittest class TestState"""
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
from models import storage


class TestState(unittest.TestCase):
    """The unittest for the model State"""

    @classmethod
    def setUpClass(cls):
        """Set up the class test"""
        pass

    @classmethod
    def tearDownClass(cls):
        """Tear down the class test"""
        pass

    def test_State(self):
        """Test the inheritance of State from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_id(self):
        """Test if id attr exist and if it's string"""
        mod = State()
        self.assertIsNotNone(mod.id)
        self.assertIsInstance(mod.id, str)
        mod2 = State()
        self.assertNotEqual(mod.id, mod2.id)

    def test_created_at(self):
        """Test if created_at attr exist and if it's a time instance"""
        mod = State()
        self.assertIsNotNone(mod.created_at)
        self.assertIsInstance(mod.created_at, type(datetime.now()))

    def test_updated_at(self):
        """Test if updated_at attr exist and if it's a time instance"""
        mod = State()
        self.assertIsNotNone(mod.updated_at)
        self.assertIsInstance(mod.updated_at, type(datetime.now()))
        self.assertNotEqual(mod.updated_at, mod.created_at)

    def test_name(self):
        """Test if name attr exist and if it's string and set value"""
        mod = State()
        self.assertIsNotNone(mod.name)
        self.assertIsInstance(mod.name, str)
        mod.name = "Ibb"
        self.assertEqual(mod.name, "Ibb")

    def test_name_set(self):
        """Test set non-string value to name atter"""
        mod = State()
        mod.name = 1234
        self.assertEqual(mod.name, 1234)
        mod.name = (12, 34)
        self.assertEqual(mod.name, (12, 34))
        mod.name = [12, 34, 56]
        self.assertEqual(mod.name, [12, 34, 56])

    def test_access_attrs(self):
        """Test the access of the public instance attributes"""
        mod = State()
        x = 12345
        self.assertNotEqual(mod.id, x)
        mod.id = 12345
        self.assertEqual(mod.id, x)
        mod.id = "Abdo"
        self.assertEqual(mod.id, "Abdo")

    def test_new_attr(self):
        """Test sets new attributes"""
        mod = State()
        mod.my_name = "Abdo"
        self.assertEqual(mod.my_name, "Abdo")
        mod.my_number = 98
        self.assertEqual(mod.my_number, 98)

    def test_str(self):
        """Test the str output of the class"""
        mod = State()
        strout = f"[{mod.__class__.__name__}] ({mod.id}) {mod.__dict__}"
        self.assertEqual(str(mod), strout)
        mod.my_name = "abdo"
        self.assertNotEqual(str(mod), strout)

    def test_save(self):
        """Test the save method"""
        mod = State()
        updat = mod.updated_at
        mod.save()
        self.assertNotEqual(mod.updated_at, updat)
        dct = storage.all()
        self.assertIn(mod, dct.values())

    def test_ot_dict(self):
        """Test the to_dict method"""
        mod = State()
        dct = mod.to_dict()
        self.assertIsInstance(dct, dict)
        self.assertIn('__class__', dct.keys())
        """test if created_at change to isoforamt"""
        self.assertTrue(dct['created_at'] != mod.created_at)
        self.assertEqual(dct['created_at'], mod.created_at.isoformat())

    def test_createNew(self):
        """Test create a new object using old dict insatance"""
        mod = State()
        dct = mod.to_dict()
        mod1 = State(**dct)
        self.assertEqual(mod.id, mod1.id)
        self.assertNotEqual(mod, mod1)
        self.assertFalse(mod == mod1)
        mod.my_name = "Abdo"
        with self.assertRaises(AttributeError):
            """AttributeError: mod1 has no attribute my_name"""
            self.assertIsNotNone(mod1.my_name)
        self.assertIsNotNone(mod.my_name)


if __name__ == "__main__":
    unittest.main()
