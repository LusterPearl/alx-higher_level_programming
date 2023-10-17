#!/usr/bin/python3
""" A first class named Base the folder will become a Python package. """

import json
import turtle
import csv

class Base:
    """
    A class that defines a Base for managing id.

    Attributes:
        width : The width of the Base
        height : The height of the Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance with optional id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of lis_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        json_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(json_list)
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                data = file.read()
                if not data:
                    return []
                instances = json.loads(data)
                return [cls.create(**inst) for inst in instances]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize objects to CSV and save to a file."""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".csv"

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls is Rectangle:
                    data = {
                        'id': obj.id,
                        'width': obj.height,
                        'x': obj.x,
                        'y': obj.y
                    }
                elif cls is Square:
                    data = {
                        'id': obj.id,
                        'size': obj.size,
                        'x': obj.x,
                        'y': obj.y
                    }
                writer.writerow([cls.to_csv(data)])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize objects from CSV file and return a list."""
        filename = cls.__name__ + ".csv"
        objects = []
        if not os.path.exists(filename):
            return objects

        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file)
            for obj_data in reader:
                obj_data = [int(data) for data in obj_data]
                if cls.__name__ == "Rectangle":
                    obj = cls(0, 0)
                else:
                    obj = cls(0)
                obj.from_csv(obj_data)
                objects.append(obj)
        return objects

    def to_csv(cls, list_objs):
        """ function to base to_csv to return json.dumps"""
        return json.dumps([obj.to_dictionary() for obj in list_objs])

    """def some_function_that_uses_rectangle():
        from models.rectangle import Rectangle
        r = Rectangle(10, 20)"""

    @staticmethod
    def draw(list_rectangles, list_squares):
        """click or daraw turtle for drawing"""
        window = turtle.Screen()
        window.bgcolor("white")

        """create a Turtle object for drawing """
        drawer = turtle.Turtle()
        drawer.shape("turtle")
        drawer.color("blue")
        drawer.speed(1)

        for rect in list_rectangles:
            drawer.penup()
            drawer.goto(rect.x, rect.y)
            drawer.pendown()
            for _ in range(2):
                drawer.forward(rect.width)
                drawer.left(90)
                drawer.forward(rect.height)
                drawer.left(90)

        for square in list_squares:
            drawer.penup()
            drawer.goto(square.x, square.y)
            drawer.pendown()
            for _ in range(4):
                drawer.forward(square.size)
                drawer.left(90)

        """Close the window on click """
        window.exitonclick()
