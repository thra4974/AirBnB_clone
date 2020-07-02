#!/usr/bin/python3
"""Test file for engine """
import unittest
import pep8
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """ tests filestorage for pep8 formatting """
    def pep_8_test(self):
        """ test filestorage and test_file_storage for pep8 formatting """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/file_storage.py'
        file2 = 'tests/test_models/test_engine/test_file_storage.py'
        res = style.check_files([file1, file2])
        self.assertEqual(res.total_errors, 0,
                         "Pep8 Errors and Warnings found")


class TestFileStorage(unittest.TestCase):
    """ Tests for FileStorage Module """
    @classmethod
    def setUpClass(cls):
        """ set up class instances for FileStorage tests """
        storage = FileStorage()

    def test_all(self):
        """ tests filestorage methods """
        pass
