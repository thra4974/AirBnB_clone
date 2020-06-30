#!/usr/bin/python3
"""class Review that inherit from BaseModel"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Review
    """
    place_id = ""
    user_id = ""
    text = ""
