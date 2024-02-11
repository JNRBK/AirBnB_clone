#!/usr/bin/python3
"""Module of BaseModel to define BaseModel class"""
from datetime import datetime
import models
import uuid


class BaseModel():
    """ The BaseModel Class """

    def __init__(self, *args, **kwargs):
        """ Initiation of objects. """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                else:
                    setattr(self, key, value)
                    if key == 'created_at':
                        self.created_at = datetime.fromisoformat(value)
                    if key == 'updated_at':
                        self.updated_at = datetime.fromisoformat(value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns the instance representation as string. """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """ updates updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns dict. containing keys/values of __dict__ of instance. """
        cp_dict = self.__dict__.copy()
        cp_dict['created_at'] = self.created_at.isoformat()
        cp_dict['updated_at'] = self.updated_at.isoformat()
        cp_dict['__class__'] = self.__class__.__name__
        return cp_dict
