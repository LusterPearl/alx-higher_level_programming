#!/usr/bin/python3
""" A function that returns a dictionary function """


def class_to_json(obj):
    """
    Return a dictionary description of a class instance for JSON.

    Args:
        obj: An instance of a class

    Returns:
        dict: A dictionary representation of the class instance.
    """
    return obj.__dict__
