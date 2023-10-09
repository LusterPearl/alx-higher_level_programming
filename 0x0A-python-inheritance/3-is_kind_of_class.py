#!/usr/bin/python3
"""
Defines a function is_kind_of class that checks if an object is an
instance or if the object is an instance of a class that inherited from,
the specifiefied class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an 
    instance of a class that inherited from, the specified class .

    Args:
        obj: he object to check.
        a_class: The class to compre with.

    Returns:
            True if obj is an instance of a_class or inherited from a_class
    """
    return isinstance(obj, a_class0
