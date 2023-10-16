#!/usr/bin/python3
""" A class Square """

"""from models.rectangle import Rectangle"""
from models.base import Base


class Square(Base):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initiliaze Square instance"""
        super().__init__(size, size, x, y, id)

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
        return "[Square ({}) {}/{} = {}".format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Returns a dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def to_csv(self):
        data = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return super().to_csv(data)

    @staticmethod
    def from_json_sring(json_string):
        """Returns the list of dictionaries represented by json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    def to_csv(self):
        """Return data for serialization to CSV format."""
        return [self.id, self.width, self.height, self.x, self.y]

    def to_csv(self, data):
        return f"{data['id']},{data['width']},{data['height']},{data['x']}, {data['y']}"
