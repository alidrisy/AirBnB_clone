#!/usr/bin/python3
"""Define the unittest class TestFileStorage"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City


class TestFileStorage(unittest.TestCase):
    """The unittest for the model FileStorage"""

    @classmethod
    def setUpClass(cls):
        """Set up the class test"""
        pass

    @classmethod
    def tearDownClass(cls):
        """Tear down the class test"""
        pass

    def test_object_attr(self):
        """Test access to calss attr __object"""
        storage.__objects = 16
        self.assertEqual(storage.__objects, 16)
        storage.__objects = "Abdo"
        self.assertEqual(storage.__objects, "Abdo")
        storage.__objects = 5.6
        self.assertEqual(storage.__objects, 5.6)

    def test_file_path_attr(self):
        """Test access to calss attr __object"""
        storage.__file_path = 16
        self.assertIsNotNone(storage.__file_path)
        self.assertEqual(storage.__file_path, 16)
        storage.__file_path = "Abdo"
        self.assertEqual(storage.__file_path, "Abdo")
        storage.__file_path = 5.6
        self.assertEqual(storage.__file_path, 5.6)

    def test_all(self):
        """Test the method all()"""
        storage.reload()
        dct = storage.all()
        self.assertIsNotNone(dct)
        self.assertIsInstance(dct, dict)

    def test_new(self):
        """Test the method new()"""
        mod = BaseModel()
        """notice: that the new called into the __init__ object method"""
        dct = storage.all()
        self.assertIn(mod, dct.values())
        """Test base value to new"""
        with self.assertRaises(AttributeError):
            storage.new(12)
        with self.assertRaises(AttributeError):
            storage.new("Abdo")

    def test_save(self):
        """Test the method save()"""
        storage.reload()
        mod = BaseModel()
        mod.my_name = "Test_model"
        storage.save()
        storage.reload()
        dct = storage.all()
        key = key = str(mod.__class__.__name__)+"."+str(mod.id)
        self.assertEqual(mod.id, dct[key].id)
        self.assertEqual(mod.my_name, dct[key].my_name)
        self.assertNotEqual(mod, dct[key])

    def test_BaseModel(self):
        """Comprehensive test of FileStorage performance with BaseModel"""
        mod = BaseModel()
        mod.my_name = "Test_Base"
        mod.save()
        dct = storage.all()
        self.assertIn(mod, dct.values())
        key = key = str(mod.__class__.__name__)+"."+str(mod.id)
        self.assertEqual(mod.id, dct[key].id)
        self.assertEqual(mod.my_name, dct[key].my_name)
        self.assertEqual(mod, dct[key])
        storage.reload()
        dct = storage.all()
        self.assertNotEqual(mod, dct[key])

    def test_User(self):
        """Comprehensive test of FileStorage performance with User"""
        mod = User()
        mod.my_name = "Test_User"
        mod.save()
        dct = storage.all()
        self.assertIn(mod, dct.values())
        key = key = str(mod.__class__.__name__)+"."+str(mod.id)
        self.assertEqual(mod.id, dct[key].id)
        self.assertEqual(mod.my_name, dct[key].my_name)
        self.assertEqual(mod, dct[key])
        storage.reload()
        dct = storage.all()
        self.assertNotEqual(mod, dct[key])

    def test_State(self):
        """Comprehensive test of FileStorage performance with State"""
        mod = State()
        mod.my_name = "Test_State"
        mod.save()
        dct = storage.all()
        self.assertIn(mod, dct.values())
        key = key = str(mod.__class__.__name__)+"."+str(mod.id)
        self.assertEqual(mod.id, dct[key].id)
        self.assertEqual(mod.my_name, dct[key].my_name)
        self.assertEqual(mod, dct[key])
        storage.reload()
        dct = storage.all()
        self.assertNotEqual(mod, dct[key])

    def test_City(self):
        """Comprehensive test of FileStorage performance with City"""
        mod = City()
        mod.my_name = "Test_City"
        mod.save()
        dct = storage.all()
        self.assertIn(mod, dct.values())
        key = key = str(mod.__class__.__name__)+"."+str(mod.id)
        self.assertEqual(mod.id, dct[key].id)
        self.assertEqual(mod.my_name, dct[key].my_name)
        self.assertEqual(mod, dct[key])
        storage.reload()
        dct = storage.all()
        self.assertNotEqual(mod, dct[key])

    def test_Amenity(self):
        """Comprehensive test of FileStorage performance with Amenity"""
        mod = Amenity()
        mod.my_name = "Test_Amenity"
        mod.save()
        dct = storage.all()
        self.assertIn(mod, dct.values())
        key = key = str(mod.__class__.__name__)+"."+str(mod.id)
        self.assertEqual(mod.id, dct[key].id)
        self.assertEqual(mod.my_name, dct[key].my_name)
        self.assertEqual(mod, dct[key])
        storage.reload()
        dct = storage.all()
        self.assertNotEqual(mod, dct[key])

    def test_Place(self):
        """Comprehensive test of FileStorage performance with Place"""
        mod = Place()
        mod.my_name = "Test_Place"
        mod.save()
        dct = storage.all()
        self.assertIn(mod, dct.values())
        key = key = str(mod.__class__.__name__)+"."+str(mod.id)
        self.assertEqual(mod.id, dct[key].id)
        self.assertEqual(mod.my_name, dct[key].my_name)
        self.assertEqual(mod, dct[key])
        storage.reload()
        dct = storage.all()
        self.assertNotEqual(mod, dct[key])

    def test_Review(self):
        """Comprehensive test of FileStorage performance with Review"""
        mod = Review()
        mod.my_name = "Test_Review"
        mod.save()
        dct = storage.all()
        self.assertIn(mod, dct.values())
        key = key = str(mod.__class__.__name__)+"."+str(mod.id)
        self.assertEqual(mod.id, dct[key].id)
        self.assertEqual(mod.my_name, dct[key].my_name)
        self.assertEqual(mod, dct[key])
        storage.reload()
        dct = storage.all()
        self.assertNotEqual(mod, dct[key])


if __name__ == "__main__":
    unittest.main()
