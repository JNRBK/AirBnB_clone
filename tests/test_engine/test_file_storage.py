#!/usr/bin/python3
""" FileStorage UnitTest Module"""
import json
from models.engine.file_storage import FileStorage
from models import storage
import unittest


class TestFileStorage(unittest.TestCase):
    """ Test FileStorage Class. """
    @classmethod
    def setUpClass(cls):
        """ Creating objects to be tested. """
        cls.f_storage = FileStorage()
        cls.path_check = cls.f_storage._FileStorage__file_path
        cls.obj_check = cls.f_storage._FileStorage__objects

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
        self.assertIsInstance(self.path_check, str)

    def test_objects(self):
        """ Testing the __objects class attribute. """
        self.assertIsInstance(self.obj_check, dict)

    def test_all(self):
        """ Testing the all method. """
        returned = self.f_storage.all()
        self.assertEqual(returned, self.obj_check)
        self.assertIsInstance(returned, dict)

    def test_new(self):
        """ Testing the new method. """
        self.f_storage.new(self)

    def test_save(self):
        """ Testing the save method. """
        pass

    def test_reload(self):
        """ Testing the reload method. """
        pass


if __name__ == '__main__':
    unittest.main()
