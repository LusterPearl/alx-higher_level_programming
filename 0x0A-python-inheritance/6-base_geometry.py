#!/usr/bin/python3
"""
Defines a class BaseGeometry with am ethod area() that raises
an Exception.
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
