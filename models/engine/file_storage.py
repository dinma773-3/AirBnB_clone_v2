#!/usr/bin/python3
"""class to manage storage"""
import json
import models


class FileStorage:
"""storage of models"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns models"""
        if (not cls):
            return self.__objects
        result = {}
        for key in self.__objects.keys():
            if (key.split(".")[0] == cls.__name__):
                result.update({key: self.__objects[key]})
        return result

    def new(self, obj):
        """new object added"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """update JSON file"""
        temp = {}
        for id, obj in self.__objects.items():
            temp[id] = obj.to_dict()
        with open(self.__file_path, "w") as json_file:
            json.dump(temp, json_file)

    def reload(self):
        """
        update dict
        """
        try:
            with open(self.__file_path, "r") as json_file:
                temp = json.load(json_file)
            for id, dict in temp.items():
                temp_instance = models.dummy_classes[dict["__class__"]](**dict)
                self.__objects[id] = temp_instance
        except:
            pass

    def close(self):
        """display data"""
        self.reload()

    def delete(self, obj=None):
        """deletes if needed
        """
        if (obj):
            self.__objects.pop("{}.{}".format(type(obj).__name__, obj.id))
