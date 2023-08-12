#!/usr/bin/python3
"""Define State class for the AirBnB"""
from models.base_model import BaseModel


class State(BaseModel):
    """The state object indicates the place
    wher the place to rent
    Args:
    name (str): the name of the state
    """

    name = ""
