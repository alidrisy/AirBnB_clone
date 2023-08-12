#!/usr/bin/python3
"""Define the unittest class TestUser"""
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    """The unittest for the model User"""

    @classmethod
    def setUpClass(cls):
        """Set up the class test"""
        pass

    @classmethod
    def tearDownClass(cls):
        """Tear down the class test"""
        pass

    def test_User(self):
        """Test the inheritance of User from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_id(self):
        """Test if id attr exist and if it's string"""
        mod = User()
        self.assertIsNotNone(mod.id)
        self.assertIsInstance(mod.id, str)
        mod2 = User()
        self.assertNotEqual(mod.id, mod2.id)

    def test_created_at(self):
        """Test if created_at attr exist and if it's a time instance"""
        mod = User()
        self.assertIsNotNone(mod.created_at)
        self.assertIsInstance(mod.created_at, type(datetime.now()))

    def test_updated_at(self):
        """Test if updated_at attr exist and if it's a time instance"""
        mod = User()
        self.assertIsNotNone(mod.updated_at)
        self.assertIsInstance(mod.updated_at, type(datetime.now()))
        self.assertNotEqual(mod.updated_at, mod.created_at)

    def test_email(self):
        """Test if email attr exist and if it's string and set value"""
        mod = User()
        self.assertIsNotNone(mod.email)
        self.assertIsInstance(mod.email, str)
        mod.email = "Abdo@gmail.com"
        self.assertEqual(mod.email, "Abdo@gmail.com")

    def test_email_set(self):
        """Test set non-string value to email atter"""
        mod = User()
        mod.email = 1234
        self.assertEqual(mod.email, 1234)
        mod.email = (12, 34)
        self.assertEqual(mod.email, (12, 34))
        mod.email = [12, 34, 56]
        self.assertEqual(mod.email, [12, 34, 56])

    def test_password(self):
        """Test if password attr exist and if it's string and set value"""
        mod = User()
        self.assertIsNotNone(mod.password)
        self.assertIsInstance(mod.password, str)
        mod.password = "A12b34"
        self.assertEqual(mod.password, "A12b34")

    def test_password_set(self):
        """Test set non-string value to password atter"""
        mod = User()
        mod.password = 1234
        self.assertEqual(mod.password, 1234)
        mod.password = (12, 34)
        self.assertEqual(mod.password, (12, 34))
        mod.password = [12, 34, 56]
        self.assertEqual(mod.password, [12, 34, 56])

    def test_first_name(self):
        """Test if first_name attr exist and if it's string and set value"""
        mod = User()
        self.assertIsNotNone(mod.first_name)
        self.assertIsInstance(mod.first_name, str)
        mod.first_name = "Abdo"
        self.assertEqual(mod.first_name, "Abdo")

    def test_first_name_set(self):
        """Test set non-string value to first_name atter"""
        mod = User()
        mod.first_name = 1234
        self.assertEqual(mod.first_name, 1234)
        mod.first_name = (12, 34)
        self.assertEqual(mod.first_name, (12, 34))
        mod.first_name = [12, 34, 56]
        self.assertEqual(mod.first_name, [12, 34, 56])

    def test_last_name(self):
        """Test if last_name attr exist and if it's string and set value"""
        mod = User()
        self.assertIsNotNone(mod.last_name)
        self.assertIsInstance(mod.last_name, str)
        mod.last_name = "Alx"
        self.assertEqual(mod.last_name, "Alx")

    def test_last_name_set(self):
        """Test set non-string value to last_name atter"""
        mod = User()
        mod.last_name = 1234
        self.assertEqual(mod.last_name, 1234)
        mod.last_name = (12, 34)
        self.assertEqual(mod.last_name, (12, 34))
        mod.last_name = [12, 34, 56]
        self.assertEqual(mod.last_name, [12, 34, 56])

    def test_access_attrs(self):
        """Test the access of the public instance attributes"""
        mod = User()
        x = 12345
        self.assertNotEqual(mod.id, x)
        mod.id = 12345
        self.assertEqual(mod.id, x)
        mod.id = "Abdo"
        self.assertEqual(mod.id, "Abdo")

    def test_new_attr(self):
        """Test sets new attributes"""
        mod = User()
        mod.my_name = "Abdo"
        self.assertEqual(mod.my_name, "Abdo")
        mod.my_number = 98
        self.assertEqual(mod.my_number, 98)

    def test_str(self):
        """Test the str output of the class"""
        mod = User()
        strout = f"[{mod.__class__.__name__}] ({mod.id}) {mod.__dict__}"
        self.assertEqual(str(mod), strout)
        mod.my_name = "abdo"
        self.assertNotEqual(str(mod), strout)

    def test_save(self):
        """Test the save method"""
        mod = User()
        updat = mod.updated_at
        mod.save()
        self.assertNotEqual(mod.updated_at, updat)
        dct = storage.all()
        self.assertIn(mod, dct.values())

    def test_ot_dict(self):
        """Test the to_dict method"""
        mod = User()
        dct = mod.to_dict()
        self.assertIsInstance(dct, dict)
        self.assertIn('__class__', dct.keys())
        """test if created_at change to isoforamt"""
        self.assertTrue(dct['created_at'] != mod.created_at)
        self.assertEqual(dct['created_at'], mod.created_at.isoformat())

    def test_createNew(self):
        """Test create a new object using old dict insatance"""
        mod = User()
        dct = mod.to_dict()
        mod1 = User(**dct)
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
