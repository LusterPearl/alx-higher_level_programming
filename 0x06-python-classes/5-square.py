#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class representing a square."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int, optional): The size (side length) of the square.
                Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size (side length) of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size (side length) of the square

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
