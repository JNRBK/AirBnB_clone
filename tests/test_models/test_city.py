#!/usr/bin/python3
""" City UnitTest Module"""
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.new_object = City()

    @classmethod
    def tearDownClass(cls):
        del cls.new_object

    def test_init(self):
        self.assertIsInstance(self.new_object, City)
        self.assertIsInstance(self.new_object, BaseModel)

    def test_type(self):
        self.assertIsInstance(self.new_object.state_id, str)
        self.assertIsInstance(self.new_object.name, str)

    def test_EmptyOrNot(self):
        self.assertFalse(self.new_object.state_id)
        self.assertFalse(self.new_object.name)


if __name__ == '__main__':
    unittest.main()
