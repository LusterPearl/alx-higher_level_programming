#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle.
"""


class Square(Rectangle):
    """
    A class representing a sqaure.
    """

    def __init__(self, size):
        """
        Initialize a square with a specified size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: The square description in the format [square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
