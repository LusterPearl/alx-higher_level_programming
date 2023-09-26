#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class representing a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (init, optional): The size (side length) of the square.
                Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
