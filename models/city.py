#!/usr/bin/python3
"""Define City class for the AirBnB"""
from models.base_model import BaseModel


class City(BaseModel):
    """The city which the place in

    Args:
        state_id (str): the state id
        name (str): the city's name
    """

    state_id = ""
    name = ""
