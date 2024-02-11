#!/usr/bin/python3
""" FileStorage UnitTest Module"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import unittest
import os.path


class TestFileStorage(unittest.TestCase):
    """ Test FileStorage Class. """

    @classmethod
    def setUpClass(cls):
        """ Creating objects to be tested. """
        cls.f_storage = FileStorage()
        cls.object = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """ Deleting objects at the end of the test"""
        del cls.f_storage

    def test_init(self):
        """ Testing the object created. """
        self.assertIsInstance(self.f_storage, FileStorage)
        self.assertTrue(self.f_storage)

    def test_fpath(self):
        """ Checking the file path of the Json file. """
        file_name = 'file.json'
        to_be_checked = os.path.isfile(FileStorage.locate_file())
        self.assertTrue(to_be_checked)

    def test_objects(self):
        """ Testing the __objects class attribute. """
        self.assertIsInstance(FileStorage.object_get(), dict)

    def test_all(self):
        """ Testing the all() method attribute. """
        self.assertIsInstance(self.f_storage.all(), dict)


if __name__ == '__main__':
    unittest.main()
