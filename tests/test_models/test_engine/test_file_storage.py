#!/usr/bin/python3
""" FileStorage UnitTest Module"""
from datetime import datetime, timedelta
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

    def test_save(self):
        """ Testing values after saving. """
        self.object.save()

        key_name = f'{self.object.__class__.__name__}.{self.object.id}'
        val = self.f_storage.all()[key_name].updated_at

        # Checking the time is same at time of saving with the saved one
        t2 = datetime.utcnow()
        time_difference = abs(val - t2)
        delta_seconds = time_difference.total_seconds()

        # Making sure BaseModel instance was saved in the storage
        # By checking the key; classname.id
        self.assertIn(key_name, self.f_storage.all())

        # Making sure object was saved correctly in storage
        # having same value of BaseModel instance; eg. updated_at
        self.assertEqual(self.object.updated_at, val)

        # Checking the time of saving of the object, "almost equal";
        # Because there's difference in time between creating the object
        # Then saving it into a file ..
        self.assertAlmostEqual(val, t2, delta=timedelta(seconds=delta_seconds))


if __name__ == '__main__':
    unittest.main()
