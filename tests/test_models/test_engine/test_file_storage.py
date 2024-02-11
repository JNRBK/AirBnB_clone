#!/usr/bin/python3
""" FileStorage UnitTest Module"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import unittest


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
        pass

    def test_objects(self):
        """ Testing the __objects class attribute. """
        pass

    def test_all(self):
        """ Testing the all method. """
        returned = self.f_storage.all()
        self.assertIsInstance(returned, dict)

    def test_new(self):
        """ Testing the new method. """
        self.f_storage.new(self)

    def test_save(self):
        """ Testing the save method. """
        self.assertTrue('file.json')

    def test_reload(self):
        """ Testing the reload method. """
        pass


if __name__ == '__main__':
    unittest.main()
