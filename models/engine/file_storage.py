#!/usr/bin/python3
""" Contains FileStorage Class """
from datetime import datetime
import json
from models.base_model import BaseModel
import models
import uuid
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Amenity": Amenity, "Place": Place,
           "Review": Review}


class FileStorage:
    """ defines Filestorage class """

    __file_path = "file"
    __objects = {}

    def all(self):
        """ returns __obj """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj w/ key <obj class name>.id """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to JSON file """
        dictionary = {}
        json_ext = ".json"
        JSON_FILE = self.__file_path + json_ext

        with open(JSON_FILE, "w+", encoding="utf-8") as f:
            for keys, values in self.__objects.items():
                dictionary[keys] = values.to_dict()
            json.dump(dictionary, f)

    def reload(self):
        """ deserializes JSON_FILE """
        json_ext = ".json"
        JSON_FILE = self.__file_path + json_ext
        try:
            with open(JSON_FILE, "r", encoding="utf-8") as f:
                load_obj = json.load(f)
                for key, values in load_obj.items():
                    re_obj = eval('{}(**values)'.format(values['__class__']))
                    self.__objects[key] = re_obj
        except IOError:
            pass
