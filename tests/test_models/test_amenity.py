#!/usr/bin/python3
import unittest
import os
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
import json


class TestBaseModelDocs(unittest.TestCase):
    """ test for docstrings """
    def test_documentation(self):
        """ class docstring test """
        self.assertTrue(len(Amenity.__doc__) > 0)


class TestBaseModelPep8(unittest.TestCase):
    """ test for pep8 formatting """
    def pep8_test(self):
        """ test base and test_base for pep8 formatting """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/amenity.py'
        file2 = 'tests/test_models/test_amenity.py'
        res = style.check_files([file1, file2])
        self.assertEqual(res.total_errors,
                         0, "Pep style errors and warnings my dog.")


class TestBaseModelClass(unittest.TestCase):
    """ test BaseModel Class methods """
    @classmethod
    def setUpClass(cls):
        """ create instance for test """
        cls.amenity = Amenity()

    def test_id(self):
        """ test id of instance """
        self.assertEqual(str, type(self.amenity.id))

    def test_created_at(self):
        """ test created_at attribute """
        self.assertEqual(datetime, type(self.amenity.created_at))

    def test_updated_at(self):
        """ test updated at attribute """
        self.assertEqual(datetime, type(self.amenity.updated_at))

    def test_to_dict(self):
        """ test to_dict method """
        dictionary = self.amenity.to_dict()
        self.assertEqual(type(dictionary), dict)
        self.assertTrue('to_dict' in dir(self.amenity))

    @classmethod
    def tearDownClass(cls):
        """ delete instance of test cases """
        pass
