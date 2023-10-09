#!/usr/bin/python3
"""
Defines a class Rectangle that inherits from BaseGeometry.
"""


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with a specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validtor("height", height)
        self.__width = width
        self.__height = height
