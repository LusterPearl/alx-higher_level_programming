#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


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
        super().__init__(size, size)
