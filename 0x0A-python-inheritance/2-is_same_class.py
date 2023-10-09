#!/usr/bin/python3
"""
Defines a function is_same_class that checks if an object is exactly an
instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj: The objet to check.
        a_class: The class to compare with.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) == a_class
