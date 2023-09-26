#!/usr/bin/python3


class Square:
    """Class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int, optional): The size (side length) of the square.
                Defaults to 0.
            position (tuple, optional): The position of the square.
                Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size (side length) of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size (size length) of the square.

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

    @property
    def position(self):
        """Get the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position as a tuple of two positive integers.

        Raises:
            TypeError: If value is not a tuple of two positive integer.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers"""
        else:
            self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Custom string representation of the Square instance."""
        result = ""
        if self.__size == 0:
            return (result)
        else:
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size + "\n"
            return result.strip()
