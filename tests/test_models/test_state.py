#!/usr/bin/python3
""" State UnitTest Module"""
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Creating objects to be tested. """
        cls.new_object = State()

    @classmethod
    def tearDownClass(cls):
        """ Deleting objects at the end of the test"""
        del cls.new_object

    def test_init(self):
        """ Testing the object created."""
        self.assertIsInstance(self.new_object, State)
        self.assertIsInstance(self.new_object, BaseModel)

    def test_type(self):
        """ Testing the type of the class attributes."""
        self.assertIsInstance(self.new_object.name, str)

    def test_EmptyOrNot(self):
        """ Testing whether the class attribute is empty/exists or not. """
        self.assertFalse(self.new_object.name)


if __name__ == '__main__':
    unittest.main()
