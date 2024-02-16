#!/usr/bin/python3
""" Review UnitTest Module"""
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """ Unittest Checking class Review """

    @classmethod
    def setUpClass(cls):
        """ Creating objects to be tested. """
        cls.new_object = Review()

    @classmethod
    def tearDownClass(cls):
        """ Deleting objects at the end of the test"""
        del cls.new_object

    def test_init(self):
        """ Testing the object created. """
        self.assertIsInstance(self.new_object, Review)
        self.assertIsInstance(self.new_object, BaseModel)

    def test_type(self):
        """ Testing the type of the class attributes."""
        self.assertIsInstance(self.new_object.place_id, str)
        self.assertIsInstance(self.new_object.user_id, str)
        self.assertIsInstance(self.new_object.text, str)

    def test_EmptyOrNot(self):
        """ Testing whether the class attribute is empty/exists or not. """
        self.assertFalse(self.new_object.place_id)
        self.assertFalse(self.new_object.user_id)
        self.assertFalse(self.new_object.text)


if __name__ == '__main__':
    unittest.main()
