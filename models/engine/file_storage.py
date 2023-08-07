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
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key =str(obj.__class__.__name__)+"."+str(obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as fp:
            json.dump(self.__objects, fp)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as fp:
                self.__objects = json.load(fp)
        finally:
            return
