#!/usr/bin/python3
"""
Module provides Class City
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class, inherits from BaseModel
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
