#!/usr/bin/python3
"""
Defines a class BaseGeometry with a method areas calculation and
integer validation.
"""


class BaseGeometry:
    """
    A class representing basic geometry.
    """

    def area(self):
        """
        Calculate the area (not implemented).

        Raises:
            Exception: Always raises an exception with the message
                     " area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
            name (str): The name of the value.
            value (int): The value to validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
