#!/usr/bin/python3
"""Define the unittest class TestReview"""
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel
from models import storage


class TestReview(unittest.TestCase):
    """The unittest for the model Review"""

    @classmethod
    def setUpClass(cls):
        """Set up the class test"""
        pass

    @classmethod
    def tearDownClass(cls):
        """Tear down the class test"""
        pass

    def test_Review(self):
        """Test the inheritance of Review from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_id(self):
        """Test if id attr exist and if it's string"""
        mod = Review()
        self.assertIsNotNone(mod.id)
        self.assertIsInstance(mod.id, str)
        mod2 = Review()
        self.assertNotEqual(mod.id, mod2.id)

    def test_created_at(self):
        """Test if created_at attr exist and if it's a time instance"""
        mod = Review()
        self.assertIsNotNone(mod.created_at)
        self.assertIsInstance(mod.created_at, type(datetime.now()))

    def test_updated_at(self):
        """Test if updated_at attr exist and if it's a time instance"""
        mod = Review()
        self.assertIsNotNone(mod.updated_at)
        self.assertIsInstance(mod.updated_at, type(datetime.now()))
        self.assertNotEqual(mod.updated_at, mod.created_at)

    def test_place_id(self):
        """Test if place_id attr exist and if it's string and set value"""
        mod = Review()
        self.assertIsNotNone(mod.place_id)
        self.assertIsInstance(mod.place_id, str)
        mod.place_id = "A12b34"
        self.assertEqual(mod.place_id, "A12b34")

    def test_place_id_set(self):
        """Test set non-string value to place_id atter"""
        mod = Review()
        mod.place_id = 1234
        self.assertEqual(mod.place_id, 1234)
        mod.place_id = (12, 34)
        self.assertEqual(mod.place_id, (12, 34))
        mod.place_id = [12, 34, 56]
        self.assertEqual(mod.place_id, [12, 34, 56])

    def test_user_id(self):
        """Test if user_id attr exist and if it's string and set value"""
        mod = Review()
        self.assertIsNotNone(mod.user_id)
        self.assertIsInstance(mod.user_id, str)
        mod.user_id = "67h789"
        self.assertEqual(mod.user_id, "67h789")

    def test_user_id_set(self):
        """Test set non-string value to user_id atter"""
        mod = Review()
        mod.user_id = 1234
        self.assertEqual(mod.user_id, 1234)
        mod.user_id = (12, 34)
        self.assertEqual(mod.user_id, (12, 34))
        mod.user_id = [12, 34, 56]
        self.assertEqual(mod.user_id, [12, 34, 56])

    def test_text(self):
        """Test if text attr exist and if it's string and set value"""
        mod = Review()
        self.assertIsNotNone(mod.text)
        self.assertIsInstance(mod.text, str)
        mod.text = "I loved the place very much."
        self.assertEqual(mod.text, "I loved the place very much.")

    def test_text_set(self):
        """Test set non-string value to text atter"""
        mod = Review()
        mod.text = 1234
        self.assertEqual(mod.text, 1234)
        mod.text = (12, 34)
        self.assertEqual(mod.text, (12, 34))
        mod.text = [12, 34, 56]
        self.assertEqual(mod.text, [12, 34, 56])

    def test_access_attrs(self):
        """Test the access of the public instance attributes"""
        mod = Review()
        x = 12345
        self.assertNotEqual(mod.id, x)
        mod.id = 12345
        self.assertEqual(mod.id, x)
        mod.id = "Abdo"
        self.assertEqual(mod.id, "Abdo")

    def test_new_attr(self):
        """Test sets new attributes"""
        mod = Review()
        mod.my_name = "Abdo"
        self.assertEqual(mod.my_name, "Abdo")
        mod.my_number = 98
        self.assertEqual(mod.my_number, 98)

    def test_str(self):
        """Test the str output of the class"""
        mod = Review()
        strout = f"[{mod.__class__.__name__}] ({mod.id}) {mod.__dict__}"
        self.assertEqual(str(mod), strout)
        mod.my_name = "abdo"
        self.assertNotEqual(str(mod), strout)

    def test_save(self):
        """Test the save method"""
        mod = Review()
        updat = mod.updated_at
        mod.save()
        self.assertNotEqual(mod.updated_at, updat)
        dct = storage.all()
        self.assertIn(mod, dct.values())

    def test_ot_dict(self):
        """Test the to_dict method"""
        mod = Review()
        dct = mod.to_dict()
        self.assertIsInstance(dct, dict)
        self.assertIn('__class__', dct.keys())
        """test if created_at change to isoforamt"""
        self.assertTrue(dct['created_at'] != mod.created_at)
        self.assertEqual(dct['created_at'], mod.created_at.isoformat())

    def test_createNew(self):
        """Test create a new object using old dict insatance"""
        mod = Review()
        dct = mod.to_dict()
        mod1 = Review(**dct)
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
