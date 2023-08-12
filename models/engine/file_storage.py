#!/usr/bin/python3
"""Define FileStorage class"""
import json
from models.main import all_mod


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
        dic1 = all_mod()
        try:
            with open(self.__file_path, 'r') as fp:
                for key, value in json.load(fp).items():
                    self.new(dic1[value['__class__']](**value))
        finally:
            return
