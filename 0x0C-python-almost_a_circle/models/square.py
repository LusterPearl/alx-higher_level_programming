#!/usr/bin/python3
""" A class Square """

from models.base import Base


class Square(Base):
    """Square class that inherits from Rectangle"""
    """
    A class that defines a square.

    Attributes:
        width (int): The width of the square.
        height (int): The height of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initiliaze Square instance"""
        super().__init__(id)
        self.size = size
        self.x = x
        self.y = y

    def update(self, *args, **kwargs):
        """Update attributes of the Square instance"""
        if args:
            attr_list = ['id', 'size', 'x', 'y']
            for i, attr in enumerate(attr_list):
                if i < len(args):
                    setattr(self, attr, args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of Square"""
        return "[Square ({}) {}/{} = {}".format(self.id,
                                                self.x, self.y, self.width)

    def to_dictionary(self):
        """Returns a dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def area(self):
        """Calculating the area of the square"""
        return self.size ** 2

    def display(self):
        """Display a visual representation of the square"""
        for _ in range(self.y):
            print()
        for _ in range(self.size):
            print(" " * self.x + "#" * self.size)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of dictionaries represented by json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    def to_csv(self):
        """Return data for serialization to CSV format."""
        return [self.id, self.width, self.height, self.x, self.y]

    def to_csv(self, data):
        return (
            f"{data['id']},"
            f"{data['width']},"
            f"{data['height']},"
            f"{data['x']},"
            f"{data['y']}"
        )
