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

    def __init__(self, *args, **kwargs):
        """Initilaize instances"""
        if kwargs is None or len(kwargs) == 0:
            super().__init__()
            self.state_id = City.state_id
            self.name = City.name
        else:
            super().__init__(**kwargs)
