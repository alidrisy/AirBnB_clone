#!/usr/bin/python3
"""Define Place class for the AirBnB"""
from models.base_model import BaseModel


class Place(BaseModel):
    """The place iformation which will rent

    Args:
        city_id (str): the city id
        user_id (str): the user id
        name (str): the place name
        description (str): the place description
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): number of gustes
        price_by_night (int): the price of rent per night
        latitude (float): the place latitude
        longitude (float): the place longitude
        amenity_ids (list): list of amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
