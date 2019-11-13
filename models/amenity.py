#!/usr/bin/python3
"""Module to inherit from BaseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel
    """
    name = ''
