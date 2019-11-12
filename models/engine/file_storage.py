#!/usr/bin/python3
"""Module that serialized and deserializes
"""


from model.base_model import BaseModel
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to
        instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file
        """
        with open(self.__file_path, 'w', encoding='utf-8') as new_file:
            json.dump(
                 {k: v.to_dict() for k, v in self.__objects.items()}, new_file)

    def reload(self):
        """Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as new_file:
                dict_new = json.loads(new_file.read())
                for value in dict_new.values():
                    clase = value["__class__"]
                    self.new(eval(clase)(**value))
        except:
            pass
