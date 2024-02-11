#!/usr/bin/python3
""" User UnitTest Module"""
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """ Unittest Checking class User """

    @classmethod
    def setUpClass(cls):
        """ Creating objects to be tested. """
        cls.new_object = User()

    @classmethod
    def tearDownClass(cls):
        """ Deleting objects at the end of the test"""
        del cls.new_object

    def test_init(self):
        """ Testing the object created. """
        self.assertIsInstance(self.new_object, User)
        self.assertIsInstance(self.new_object, BaseModel)

    def test_type(self):
        """ Testing the type of the class attributes."""
        self.assertIsInstance(self.new_object.email, str)
        self.assertIsInstance(self.new_object.password, str)
        self.assertIsInstance(self.new_object.first_name, str)
        self.assertIsInstance(self.new_object.last_name, str)

    def test_EmptyOrNot(self):
        """ Testing whether the class attribute is empty/exists or not. """
        self.assertFalse(self.new_object.email)
        self.assertFalse(self.new_object.password)
        self.assertFalse(self.new_object.first_name)
        self.assertFalse(self.new_object.last_name)


if __name__ == '__main__':
    unittest.main()
