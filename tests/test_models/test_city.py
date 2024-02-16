#!/usr/bin/python3
""" City UnitTest Module"""
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """ Unittest Checking class City """

    @classmethod
    def setUpClass(cls):
        """ Creating objects to be tested. """
        cls.new_object = City()

    @classmethod
    def tearDownClass(cls):
        """ Deleting objects at the end of the test"""
        del cls.new_object

    def test_init(self):
        """ Testing the object created. """
        self.assertIsInstance(self.new_object, City)
        self.assertIsInstance(self.new_object, BaseModel)

    def test_type(self):
        """ Testing the type of the class attributes."""
        self.assertIsInstance(self.new_object.state_id, str)
        self.assertIsInstance(self.new_object.name, str)

    def test_EmptyOrNot(self):
        """ Testing whether the class attribute is empty/exists or not. """
        self.assertFalse(self.new_object.state_id)
        self.assertFalse(self.new_object.name)


if __name__ == '__main__':
    unittest.main()
