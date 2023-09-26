#!/usr/bin/python3


class Square:
    """Class representing a square."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int or float, optional): The size of the square.
                Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int or float): The size value to set.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison based on the square's area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison based on the square's area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison based on the square's area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison based on the square's area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison based on the square's area"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison based on the square's area"""
        return self.area() >= other.area()
