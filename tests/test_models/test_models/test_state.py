#!/usr/bin/python3
""" State UnitTest Module"""
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.new_object = State()

    @classmethod
    def tearDownClass(cls):
        del cls.new_object

    def test_init(self):
        self.assertIsInstance(self.new_object, State)
        self.assertIsInstance(self.new_object, BaseModel)

    def test_type(self):
        self.assertIsInstance(self.new_object.name, str)

    def test_EmptyOrNot(self):
        self.assertFalse(self.new_object.name)


if __name__ == '__main__':
    unittest.main()
