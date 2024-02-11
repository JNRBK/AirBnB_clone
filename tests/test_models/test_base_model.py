#!/usr/bin/python3
""" BaseModel UnitTest Module"""
from datetime import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """ Unittest Checking class BaseModel """

    @classmethod
    def setUpClass(cls):
        """ Creating objects to be tested. """
        cls.object = BaseModel()
        cls.object.name = "First_Model"
        cls.object.my_number = 89

    @classmethod
    def tearDownClass(cls):
        """ Deleting objects at the end of the test"""
        del cls.object

    def test_init(self):
        """ Testing the object created. """
        self.assertIsInstance(self.object, BaseModel)
        self.assertNotIn('__class__', self.object.__dict__)

    def test_id(self):
        """ Testing the object id. """
        self.assertTrue(self.object.id)
        self.assertIsInstance(self.object.id, str)

    def test_created_at(self):
        """ Testing the created_at attribute. """
        self.assertTrue(self.object.created_at)
        self.assertIsInstance(self.object.created_at, datetime)

    def test_updated_at(self):
        """ Testing the updated_at attribute. """
        self.assertTrue(self.object.updated_at)
        self.assertIsInstance(self.object.updated_at, datetime)

    def test_save(self):
        """ Testing the save() method. """
        self.object.save()
        self.assertIsInstance(self.object.updated_at, datetime)
        self.assertNotEqual(self.object.created_at, self.object.updated_at)

    def test_to_dict(self):
        """ Testing the to_dict() method. """
        converted_dash = self.object.to_dict()
        converted_dash["Book Title"] = "A River in Darkness"
        converted_dash["Author's Name"] = "Masaji Ishikawa"
        self.object2 = BaseModel(**converted_dash)

        self.assertTrue(converted_dash['id'])
        self.assertTrue(converted_dash['__class__'])
        self.assertTrue(converted_dash['created_at'])
        self.assertTrue(converted_dash['updated_at'])

        self.assertIsInstance(converted_dash['id'], str)
        self.assertIsInstance(converted_dash['__class__'], str)
        self.assertIsInstance(converted_dash['created_at'], str)
        self.assertIsInstance(converted_dash['updated_at'], str)

        self.assertTrue(self.object2.to_dict()['id'])
        self.assertTrue(self.object2.to_dict()['__class__'])
        self.assertTrue(self.object2.to_dict()['created_at'])
        self.assertTrue(self.object2.to_dict()['updated_at'])

        self.assertIsInstance(self.object2.to_dict()['id'], str)
        self.assertIsInstance(self.object2.to_dict()['__class__'], str)
        self.assertIsInstance(self.object2.to_dict()['created_at'], str)
        self.assertIsInstance(self.object2.to_dict()['updated_at'], str)

    def test_str(self):
        """ Testing the string representation. """
        class_name = self.object.__class__.__name__
        output = f"[{class_name}] ({self.object.id}) {self.object.__dict__}"
        self.assertEqual(self.object.__str__(), output)


if __name__ == '__main__':
    unittest.main()
