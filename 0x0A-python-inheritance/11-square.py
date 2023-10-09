#!/usr/bin/python3
"""
A module that defines a class Square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a Square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Rectangle a string representation of the square.

        Returns:
            str: A  string in the format '[Square]'.
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
