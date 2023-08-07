#!/usr/bin/python3
"""Define a class BaseModel"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initilaize instances"""
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
        all_objs = storage.all()
        x = 0
        if all_objs != {}:
            for key, val in all_objs.items():
                if self.id == val['id']:
                    x = 1
            if x == 0:
                storage.new(self)
        else:
            storage.new(self)

    def __str__(self):
        """Print/Return [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance .. by using self.__dict__"""
        dict1 = dict(self.__dict__)
        dict1['updated_at'] = dict1['updated_at'].isoformat()
        dict1['created_at'] = dict1['created_at'].isoformat()
        dict1['__class__'] = self.__class__.__name__
        return dict1
