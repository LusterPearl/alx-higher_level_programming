#!/usr/bin/python3
""" Function that create an object """

import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON  file to read.

    Returns:
        Any: The Python object represented by the JSON  data in the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
