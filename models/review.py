#!/usr/bin/python3
""" contains State class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ inherits from BaseModel """
    place_id = ""
    user_id = ""
    test = ""
