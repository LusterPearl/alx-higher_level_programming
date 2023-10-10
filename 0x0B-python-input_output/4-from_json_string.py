#!/usr/bin/python3
""" A function that returns an object """

import json


def from_json_string(my_str):
    """
    Return an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        Any: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
