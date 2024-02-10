#!/usr/bin/python3
""" FileStorage Module """
import json


class FileStorage():
    """
    The FileStorage Class

    Attributes:
        __file_path: path to the JSON file.
        __objects: store all objects by "class name.id".
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects. """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key "obj.class name.id". """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file. """
        obj_dict_to_json = {}
        with open(FileStorage.__file_path, 'w') as file:
            for key, value in FileStorage.__objects.items():
                obj_dict_to_json[key] = value.to_dict()
            json.dump(obj_dict_to_json, file)

    def reload(self):
        """ Deserializes the JSON file to __objects. """
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        try:
            with open(FileStorage.__file_path, 'r') as file:
                loaded = json.load(file)
                for value in loaded.values():
                    try:
                        self.new(eval(value['__class__'])(**value))
                    except NameError:
                        pass
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
        # except json.decoder.JSONDecodeError:
        #     pass
