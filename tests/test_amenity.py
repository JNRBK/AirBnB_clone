#!/usr/bin/python3
""" Amenity UnitTest Module"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.new_object = Amenity()

    @classmethod
    def tearDownClass(cls):
        del cls.new_object

    def test_init(self):
        self.assertIsInstance(self.new_object, Amenity)
        self.assertIsInstance(self.new_object, BaseModel)

    def test_type(self):
        self.assertIsInstance(self.new_object.name, str)

    def test_EmptyOrNot(self):
        self.assertFalse(self.new_object.name)


if __name__ == '__main__':
    unittest.main()
