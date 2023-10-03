#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """
    A class that defines a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (in): The height of the rectangle.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance

        Args:
            width (int, optional): The width of the rectangle.
            height (int, optional): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attributes

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >- 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle

        Returns:
            str: A string representing the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = ""
        for i in range(self.__height):
            rect_str += "#" * self.__width
            if i < self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """
        Return a string representation of the rectangle for eval().

        Returns:
            str: A sring representing the rectangle in a format for eval
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method called when an instance is deleted
        Prints the message "Bye rectangle...".
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the one with bigger area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instances.

        Returns:
            Rectangle: The rectangle with bigger area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new square Rectangle instance with equal width and height.

        Args:
            size (int, optional): The size of the square.

        Returns:
            Rectangle: A new Rectangle instance reprensenting square.
        """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be >= 0")

        return cls(size, size)
