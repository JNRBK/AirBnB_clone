#!/usr/bin/python3
""" Place UnitTest Module"""
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.new_object = Place()

    @classmethod
    def tearDownClass(cls):
        del cls.new_object

    def test_init(self):
        self.assertIsInstance(self.new_object, Place)
        self.assertIsInstance(self.new_object, BaseModel)

    def test_type(self):
        self.assertIsInstance(self.new_object.city_id, str)
        self.assertIsInstance(self.new_object.user_id, str)
        self.assertIsInstance(self.new_object.name, str)
        self.assertIsInstance(self.new_object.description, str)

        self.assertIsInstance(self.new_object.number_rooms, int)
        self.assertIsInstance(self.new_object.number_bathrooms, int)
        self.assertIsInstance(self.new_object.max_guest, int)
        self.assertIsInstance(self.new_object.price_by_night, int)

        self.assertIsInstance(self.new_object.latitude, float)
        self.assertIsInstance(self.new_object.longitude, float)

        self.assertIsInstance(self.new_object.amenity_ids, list)

    def test_EmptyOrNot(self):
        self.assertFalse(self.new_object.city_id)
        self.assertFalse(self.new_object.user_id)
        self.assertFalse(self.new_object.name)
        self.assertFalse(self.new_object.description)

        self.assertFalse(self.new_object.number_rooms)
        self.assertFalse(self.new_object.number_bathrooms)
        self.assertFalse(self.new_object.max_guest)
        self.assertFalse(self.new_object.price_by_night)

        self.assertFalse(self.new_object.latitude)
        self.assertFalse(self.new_object.longitude)

        self.assertFalse(self.new_object.amenity_ids)


if __name__ == '__main__':
    unittest.main()
