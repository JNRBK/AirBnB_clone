#!/usr/bin/python3
""" User UnitTest Module"""
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.new_object = User()

    @classmethod
    def tearDownClass(cls):
        del cls.new_object

    def test_init(self):
        self.assertIsInstance(self.new_object, User)
        self.assertIsInstance(self.new_object, BaseModel)

    def test_type(self):
        self.assertIsInstance(self.new_object.email, str)
        self.assertIsInstance(self.new_object.password, str)
        self.assertIsInstance(self.new_object.first_name, str)
        self.assertIsInstance(self.new_object.last_name, str)

    def test_EmptyOrNot(self):
        self.assertFalse(self.new_object.email)
        self.assertFalse(self.new_object.password)
        self.assertFalse(self.new_object.first_name)
        self.assertFalse(self.new_object.last_name)


if __name__ == '__main__':
    unittest.main()
