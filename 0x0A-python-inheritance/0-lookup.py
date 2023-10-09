#!/usr/bin/python3
""" Defines a method with a return list. """


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)
