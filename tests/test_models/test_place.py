#!/usr/bin/python3
"""Define the unittest class TestPlace"""
import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel
from models import storage


class TestPlace(unittest.TestCase):
    """The unittest for the model Place"""

    @classmethod
    def setUpClass(cls):
        """Set up the class test"""
        pass

    @classmethod
    def tearDownClass(cls):
        """Tear down the class test"""
        pass

    def test_Place(self):
        """Test the inheritance of Place from BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_id(self):
        """Test if id attr exist and if it's string"""
        mod = Place()
        self.assertIsNotNone(mod.id)
        self.assertIsInstance(mod.id, str)
        mod2 = Place()
        self.assertNotEqual(mod.id, mod2.id)

    def test_created_at(self):
        """Test if created_at attr exist and if it's a time instance"""
        mod = Place()
        self.assertIsNotNone(mod.created_at)
        self.assertIsInstance(mod.created_at, type(datetime.now()))

    def test_updated_at(self):
        """Test if updated_at attr exist and if it's a time instance"""
        mod = Place()
        self.assertIsNotNone(mod.updated_at)
        self.assertIsInstance(mod.updated_at, type(datetime.now()))
        self.assertNotEqual(mod.updated_at, mod.created_at)

    def test_city_id(self):
        """Test if city_id attr exist and if it's string and set value"""
        mod = Place()
        self.assertIsNotNone(mod.city_id)
        self.assertIsInstance(mod.city_id, str)
        mod.city_id = "A12b34"
        self.assertEqual(mod.city_id, "A12b34")

    def test_city_id_set(self):
        """Test set non-string value to city_id atter"""
        mod = Place()
        mod.city_id = 1234
        self.assertEqual(mod.city_id, 1234)
        mod.city_id = (12, 34)
        self.assertEqual(mod.city_id, (12, 34))
        mod.city_id = [12, 34, 56]
        self.assertEqual(mod.city_id, [12, 34, 56])

    def test_user_id(self):
        """Test if user_id attr exist and if it's string and set value"""
        mod = Place()
        self.assertIsNotNone(mod.user_id)
        self.assertIsInstance(mod.user_id, str)
        mod.user_id = "67h789"
        self.assertEqual(mod.user_id, "67h789")

    def test_user_id_set(self):
        """Test set non-string value to user_id atter"""
        mod = Place()
        mod.user_id = 1234
        self.assertEqual(mod.user_id, 1234)
        mod.user_id = (12, 34)
        self.assertEqual(mod.user_id, (12, 34))
        mod.user_id = [12, 34, 56]
        self.assertEqual(mod.user_id, [12, 34, 56])

    def test_name(self):
        """Test if name attr exist and if it's string and set value"""
        mod = Place()
        self.assertIsNotNone(mod.name)
        self.assertIsInstance(mod.name, str)
        mod.name = "home"
        self.assertEqual(mod.name, "home")

    def test_name_set(self):
        """Test set non-string value to name atter"""
        mod = Place()
        mod.name = 1234
        self.assertEqual(mod.name, 1234)
        mod.name = (12, 34)
        self.assertEqual(mod.name, (12, 34))
        mod.name = [12, 34, 56]
        self.assertEqual(mod.name, [12, 34, 56])

    def test_description(self):
        """Test if description attr exist and if it's string and set value"""
        mod = Place()
        self.assertIsNotNone(mod.description)
        self.assertIsInstance(mod.description, str)
        mod.description = "Spacious house with sea view"
        self.assertEqual(mod.description, "Spacious house with sea view")

    def test_number_rooms(self):
        """Test if number_rooms attr exist and set value"""
        mod = Place()
        self.assertIsNotNone(mod.number_rooms)
        self.assertIsInstance(mod.number_rooms, int)
        mod.number_rooms = 4
        self.assertEqual(mod.number_rooms, 4)

    def test_number_rooms_set(self):
        """Test set non-integer value to number_rooms atter"""
        mod = Place()
        mod.number_rooms = "5"
        self.assertEqual(mod.number_rooms, "5")
        mod.number_rooms = (12, 34)
        self.assertEqual(mod.number_rooms, (12, 34))
        mod.number_rooms = [12, 34, 56]
        self.assertEqual(mod.number_rooms, [12, 34, 56])
        mod.number_rooms = 5.1
        self.assertEqual(mod.number_rooms, 5.1)

    def test_number_bathrooms(self):
        """Test if number_bathrooms attr exist and set value"""
        mod = Place()
        self.assertIsNotNone(mod.number_bathrooms)
        self.assertIsInstance(mod.number_bathrooms, int)
        mod.number_bathrooms = 3
        self.assertEqual(mod.number_bathrooms, 3)

    def test_number_bathrooms_set(self):
        """Test set non-integer value to number_bathrooms atter"""
        mod = Place()
        mod.number_bathrooms = "5"
        self.assertEqual(mod.number_bathrooms, "5")
        mod.number_bathrooms = (12, 34)
        self.assertEqual(mod.number_bathrooms, (12, 34))
        mod.number_bathrooms = [12, 34, 56]
        self.assertEqual(mod.number_bathrooms, [12, 34, 56])
        mod.number_bathrooms = 5.1
        self.assertEqual(mod.number_bathrooms, 5.1)

    def test_max_guest(self):
        """Test if max_guest attr exist and set value"""
        mod = Place()
        self.assertIsNotNone(mod.max_guest)
        self.assertIsInstance(mod.max_guest, int)
        mod.max_guest = 7
        self.assertEqual(mod.max_guest, 7)

    def test_max_guest_set(self):
        """Test set non-integer value to max_guest atter"""
        mod = Place()
        mod.max_guest = "5"
        self.assertEqual(mod.max_guest, "5")
        mod.max_guest = (12, 34)
        self.assertEqual(mod.max_guest, (12, 34))
        mod.max_guest = [12, 34, 56]
        self.assertEqual(mod.max_guest, [12, 34, 56])
        mod.max_guest = 5.1
        self.assertEqual(mod.max_guest, 5.1)

    def test_description_set(self):
        """Test set non-string value to description atter"""
        mod = Place()
        mod.description = 1234
        self.assertEqual(mod.description, 1234)
        mod.description = (12, 34)
        self.assertEqual(mod.description, (12, 34))
        mod.description = [12, 34, 56]
        self.assertEqual(mod.description, [12, 34, 56])

    def test_price_by_night(self):
        """Test if price_by_night attr exist and set value"""
        mod = Place()
        self.assertIsNotNone(mod.price_by_night)
        self.assertIsInstance(mod.price_by_night, int)
        mod.price_by_night = 700
        self.assertEqual(mod.price_by_night, 700)

    def test_price_by_night_set(self):
        """Test set non-integer value to price_by_night atter"""
        mod = Place()
        mod.price_by_night = "5"
        self.assertEqual(mod.price_by_night, "5")
        mod.price_by_night = (12, 34)
        self.assertEqual(mod.price_by_night, (12, 34))
        mod.price_by_night = [12, 34, 56]
        self.assertEqual(mod.price_by_night, [12, 34, 56])
        mod.price_by_night = 5.1
        self.assertEqual(mod.price_by_night, 5.1)

    def test_latitude(self):
        """Test if latitude attr exist and set value"""
        mod = Place()
        self.assertIsNotNone(mod.latitude)
        self.assertIsInstance(mod.latitude, float)
        mod.latitude = 6.5
        self.assertEqual(mod.latitude, 6.5)

    def test_latitude(self):
        """Test set non-integer value to latitude atter"""
        mod = Place()
        mod.latitude = "5"
        self.assertEqual(mod.latitude, "5")
        mod.latitude = (12, 34)
        self.assertEqual(mod.latitude, (12, 34))
        mod.latitude = [12, 34, 56]
        self.assertEqual(mod.latitude, [12, 34, 56])
        mod.latitude = 5
        self.assertEqual(mod.latitude, 5)

    def test_longitude(self):
        """Test if longitude attr exist and set value"""
        mod = Place()
        self.assertIsNotNone(mod.longitude)
        self.assertIsInstance(mod.longitude, float)
        mod.longitude = 6.5
        self.assertEqual(mod.longitude, 6.5)

    def test_longitude(self):
        """Test set non-integer value to longitude atter"""
        mod = Place()
        mod.longitude = "5"
        self.assertEqual(mod.longitude, "5")
        mod.longitude = (12, 34)
        self.assertEqual(mod.longitude, (12, 34))
        mod.longitude = [12, 34, 56]
        self.assertEqual(mod.longitude, [12, 34, 56])
        mod.longitude = 5
        self.assertEqual(mod.longitude, 5)

    def test_amenity_ids(self):
        """Test if amenity_ids attr exist and set value"""
        mod = Place()
        self.assertIsNotNone(mod.amenity_ids)
        self.assertIsInstance(mod.amenity_ids, list)
        mod.amenity_ids = ["hty67", "56yt7", "g67g5"]
        self.assertEqual(mod.amenity_ids, ["hty67", "56yt7", "g67g5"])

    def test_amenity_ids(self):
        """Test set non-list value to amenity_ids atter"""
        mod = Place()
        mod.amenity_ids = "a87bg"
        self.assertEqual(mod.amenity_ids, "a87bg")
        mod.amenity_ids = (12, 34)
        self.assertEqual(mod.amenity_ids, (12, 34))
        mod.amenity_ids = 1.65
        self.assertEqual(mod.amenity_ids, 1.65)
        mod.amenity_ids = 5
        self.assertEqual(mod.amenity_ids, 5)

    def test_access_attrs(self):
        """Test the access of the public instance attributes"""
        mod = Place()
        x = 12345
        self.assertNotEqual(mod.id, x)
        mod.id = 12345
        self.assertEqual(mod.id, x)
        mod.id = "Abdo"
        self.assertEqual(mod.id, "Abdo")

    def test_new_attr(self):
        """Test sets new attributes"""
        mod = Place()
        mod.my_name = "Abdo"
        self.assertEqual(mod.my_name, "Abdo")
        mod.my_number = 98
        self.assertEqual(mod.my_number, 98)

    def test_str(self):
        """Test the str output of the class"""
        mod = Place()
        strout = f"[{mod.__class__.__name__}] ({mod.id}) {mod.__dict__}"
        self.assertEqual(str(mod), strout)
        mod.my_name = "abdo"
        self.assertNotEqual(str(mod), strout)

    def test_save(self):
        """Test the save method"""
        mod = Place()
        updat = mod.updated_at
        mod.save()
        self.assertNotEqual(mod.updated_at, updat)
        dct = storage.all()
        self.assertIn(mod, dct.values())

    def test_ot_dict(self):
        """Test the to_dict method"""
        mod = Place()
        dct = mod.to_dict()
        self.assertIsInstance(dct, dict)
        self.assertIn('__class__', dct.keys())
        """test if created_at change to isoforamt"""
        self.assertTrue(dct['created_at'] != mod.created_at)
        self.assertEqual(dct['created_at'], mod.created_at.isoformat())

    def test_createNew(self):
        """Test create a new object using old dict insatance"""
        mod = Place()
        dct = mod.to_dict()
        mod1 = Place(**dct)
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
