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

    def __init__(self, *args, **kwargs):
        """Initilaize instances"""
        if kwargs is None or len(kwargs) == 0:
            super().__init__()
            self.place_id = Review.place_id
            self.user_id = Review.user_id
            self.text = Review.text
        else:
            super().__init__(**kwargs)
