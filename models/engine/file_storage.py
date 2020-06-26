#!/usr/bin/python3
""" Contains FileStorage Class """
from datetime import datetime
import json
from models.base_model import BaseModel
import models
import uuid


class FileStorage:
    """ defines Filestorage class """

    def __init__(self, __file_path, __objects):
        """ initializes FileStorage class
        Args:
            __file_path: string - path to JSON file
            __objects: dictionary - empty but stores all objects by 

        """
        self.__file_path = __file_path
        self.__objects = {}

    @property
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
        JSON_FILE = self.__file_path  + json_ext

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
