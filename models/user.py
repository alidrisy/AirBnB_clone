#!/usr/bin/python3
"""Define User class for the AirBnB"""
from models.base_model import BaseModel


class User(BaseModel):
    """The user information in AirBnB
    Args:
        emial (str): the user emial
        password (str): the emial password
        first_name (str): the user's first name
        last_name (str): the user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
