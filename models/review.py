#!/usr/bin/python3
"""Define Review class for the AirBnB"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The Review object for reviews the place
    Args:
        place_id (str): the place id
        user_id (str): the user id
        text (str): the review
    """

    place_id = ""
    user_id = ""
    text = ""
