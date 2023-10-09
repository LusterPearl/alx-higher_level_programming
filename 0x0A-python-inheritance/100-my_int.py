#!/usr/bin/python3
"""
A module that defines a class MyInt.
"""


class MyInt(int):
    """
    A class that defines a custom integer class Myint.
    """

    def __eq__(self, other):
        """
        Inverts the equality (==) operator.

        Args:
            other: The other value to to compare with.

        Returns:
            bool: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the inequality (!=) operator.

        Args:
            other: The other value to compare with.

        Returns:
            bool: True if equal, False if not equal
        """
        return super().__eq__(other)
