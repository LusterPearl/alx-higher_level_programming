#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class representing a square."""

    def__init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int, optional): The size (side length) of the square.
                Defaults to 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
