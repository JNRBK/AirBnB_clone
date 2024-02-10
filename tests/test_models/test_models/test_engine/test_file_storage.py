#!/usr/bin/python3
""" FileStorage UnitTest Module"""
import json
from models.engine.file_storage import FileStorage
from models import storage
import unittest


class TestFileStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.f_storage = FileStorage()
        cls.path_check = cls.f_storage._FileStorage__file_path
        cls.obj_check = cls.f_storage._FileStorage__objects

    @classmethod
    def tearDownClass(cls):
        del cls.f_storage

    def test_init(self):
        self.assertIsInstance(self.f_storage, FileStorage)
        self.assertTrue(self.f_storage)

    def test_fpath(self):
        self.assertIsInstance(self.path_check, str)


    def test_objects(self):
        self.assertIsInstance(self.obj_check, dict)
        # self.assert(self.obj_check, )

    def test_all(self):
        returned = self.f_storage.all()
        self.assertEqual(returned, self.obj_check)
        self.assertIsInstance(returned, dict)

    def test_new(self):
        # print(self.f_storage.new(self))
        # key = "{}.{}".format(updated.__class__.__name__, updated.id)
        # self.assertIn(key, updated)
        self.f_storage.new(self)
        # print(self.f_storage)
        # print(self.f_storage.__dict__)

    def test_save(self):
        pass
        # saved = self.f_storage.save()

    def test_reload(self):
        all_objs = storage.reload()
        with self.assertRaises(FileNotFoundError):
            with open(self.path_check) as file:
                file.read()
        # for obj_id in all_objs.keys():
        #     obj = all_objs[obj_id]
        #     self.assertIsInstance(obj.to_dict(), dict)
        # self.assertIsInstance(all_objs, dict)
