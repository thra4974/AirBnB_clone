#!/usr/bin/python3
"""Contains the module BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ defines class BaseModel """
    def __init__(self, id=uuid, created_at=0, updated_at=0):
        """
        initializes Base model

        Args:
        id: unique id of instance
        created_at: datetime of creation
        updated_at: datetime of update

        Return:
        None
        """

        self.id = str(id.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ string representation of BaseModel """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ updates updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
