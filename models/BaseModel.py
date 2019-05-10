#!/usr/bin/python3
"""
Contains class BaseModel
"""

from os import getenv
import uuid


class BaseModel:
    """The BaseModel class from which future classes will be derived"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.to_dict())

    def update(self, ignore, *args, **kwargs):
        """updates the instance using a dictionary of kwargs"""
        for k, v in kwargs.items():
            if k in ignore:
                continue
            setattr(self, k, v)

    def to_dict(self, save_pass=False):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
