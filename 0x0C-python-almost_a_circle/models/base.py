#!/usr/bin/python3
""" A first claas named Base. """

import json


class Base:
    """Base class for managing id attribute"""


    __nb_objects = 0


    def __init__(self, id=None)
        """Initialize Base instance with optional id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of lis_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
