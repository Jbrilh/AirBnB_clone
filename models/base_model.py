#!/usr/bin/python3
"""Basemodel class the base of the project"""
import uuid
from datetime import datetime


class BaseModel:
    """Basemodel class defines all common attributes
       and methods for other classes.
    """
    def __init__(self):
        """basemodel class inintalized"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return the string rep of the class"""
        return "[{}] ({}) <{}>".format(self.__class__.__name__,
                                       self.id, self.__dict__)

    def save(self):
        """function to update the updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary key/value pair of __dict__"""
        obj_dict = {
                'id': self.id,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat(),
                '__class__': self.__class__.__name__
                }

        for key, value in self.__dict__.items():
            if key not in obj_dict:
                obj_dict[key] = value

        return obj_dict
