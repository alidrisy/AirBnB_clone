#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):

    name = ""

    def __init__(self, *args, **kwargs):
        """Initilaize instances"""
        if kwargs is None or len(kwargs) == 0:
            super().__init__()
            self.name = Amenity.name
        else:
            super().__init__(**kwargs)
