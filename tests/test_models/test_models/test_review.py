#!/usr/bin/python3
""" Review UnitTest Module"""
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.new_object = Review()

    @classmethod
    def tearDownClass(cls):
        del cls.new_object

    def test_init(self):
        self.assertIsInstance(self.new_object, Review)
        self.assertIsInstance(self.new_object, BaseModel)

    def test_type(self):
        self.assertIsInstance(self.new_object.place_id, str)
        self.assertIsInstance(self.new_object.user_id, str)
        self.assertIsInstance(self.new_object.text, str)

    def test_EmptyOrNot(self):
        self.assertFalse(self.new_object.place_id)
        self.assertFalse(self.new_object.user_id)
        self.assertFalse(self.new_object.text)


if __name__ == '__main__':
    unittest.main()
