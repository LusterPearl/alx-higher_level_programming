#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """
    A class that defines a custom list.

    Methods:
        print_sorted(): Prints the list in ascending order.
    """

    def print_sorted(self):
        """Print the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
