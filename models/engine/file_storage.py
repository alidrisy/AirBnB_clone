#!/usr/bin/python3
"""Define FileStorage class"""
import json


class FileStorage:
    """Serializes instances to a JSON file
    and deserializes JSON file to instances
    Args:
        __file_path (str): path to the JSON file
        __objects (dict): empty but will store all objects by <class name>.id
        """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = str(obj.__class__.__name__)+"."+str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dict1 = {}
        for key, value in self.__objects.items():
            dict1[key] = value.to_dict()
        with open(self.__file_path, 'w') as fp:
            json.dump(dict1, fp)

    def reload(self):
        """deserializes the JSON file to __objects"""
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

        try:
            with open(self.__file_path, 'r') as fp:
                for key, value in json.load(fp).items():
                    self.new(dict1[value['__class__']](**value))
        finally:
            return
