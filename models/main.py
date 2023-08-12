#!/usr/bin/python3
""" get all models """


def all_mod():
    """return dict of models"""
    from models.base_model import BaseModel
    from models.user import User
    from models.review import Review
    from models.place import Place
    from models.state import State
    from models.amenity import Amenity
    from models.city import City
    dict1 = {'BaseModel': BaseModel, 'User': User, 'Review': Review}
    d = {'Place': Place, 'State': State, 'Amenity': Amenity, 'City': City}
    dict1.update(d)
    return dict1
