#!/usr/bin/python3
"""
A module that defines a function add_attribute.
"""


def add_attribute(obj, attribute, value):
    """
    Add a new attribute to an object if possible


    Args:
        obj: The object to add the attribute to.
        attribute (str): The name of the attribute.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
