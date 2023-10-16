import unittest
from models.base import Base
import json
import os
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    def test_base_constructor_with_id(self):
        b = Base(42)
        self.assertEqual(b.id, 42)

    def test_base_constructor_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_to_json_string_empty(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_non_empty(self):
        dictionaries = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}]
        json_string = Base.to_json_string(dictionaries)
        self.assertEqual(json_string, '[{"x": 1, "y": 2}, {"x": 3, "y": 4}]')

    def test_to_json_string(self):
        """ Test with a list of dictionaries """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(json_string, '[{"x": 2, "width": 10,
                                        "id": 1, "height": 7, "y": 8}]')

        """ Test with an empty list ."""
        empty_list = []
        json_string = Base.to_json_string(empty_list)
        self.assertEqual(json_string, '[]')

        """ Test with None """
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

        """ Test when list_dictionaires is empty """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

        """ Test when list_dictionaries is not empty """
        rect1 = Rectangle(10, 20)
        rect2 = Rectangle(5, 5)
        rect1_dict = rect1.to_dictionary()
        rect2_dict - rect2.to_dictionary()
        result = Base.to_json_string([rect1_dict, rect2_dict])
        expected = json.dumps([rect1_dict, rect2_dict])
        self.assertEqual(result, expected)

    def test_save_to_file(self):
        """ clean up an existing JSON files """
        for cls in [Base, Rectangle, Square]:
            filename = cls.__name__ + ".json"
            if os.path.exists(filename):
                os.remove(filename)

        """ Test save_to_file with Rectangle instance """
        rect1 = Rectangle(10, 20)
        rect2 = Rectangle(5, 5)
        Rectangle.save_to_file([rect1, rect2])

        with open("Rectangle.json", "r") as file:
            result = file.read()
            expected = Base.to_json_string([rect1.to_dictionary(),
                                            rect2.to_dictionary()])
            self.assertEqual(result, expected)

        """Test save_to_file with Square instances. """
        square1 = Square(5)
        square2 = Square(2, 2)
        Square.save_to_file([square1, square2])

        with open("Square.json", "r") as file:
            result = file.read()
            expected = Base.to_json_string([square1.to_dictionary(),
                                            square2.to_dictionary()])
            self.assertEqual(result, expected)

        """ clean up any created JSON file """
        for cls[Base, Rectangle, Square]:
            filename = clas.__name__ + ".json"
            if os.path.exists(filename):
                os.remove(filename)

        """ Test with a valid JSON string """
        json_string = '[["id": 1, "name": "Alice"}, {"id": 2, "name": Bob"}]'
        result = Base.from_json_string(json_string)
        expected = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        self.assertEqual(result, expected)

        """ Test with an empty JSON string """
        json_string = '[]'
        result = Base.from_json_string(json_string)
        expected = []
        self.assertEqual(result, expected)

        """ Test with None """
        result = Base.from_json_string(None)
        expected = []
        self.assertEqual(result, expected)

    def test_create_rectangle(self):
        """ Test creating a Rectangle from a dictionary """
        r1_dictionary = {'id': 1, 'width': 3, 'height': 5, 'x': 1, 'y': 0}
        r1 = Rectangle.create(**r1_dictionary)
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 3)
        self.asseertEqual(r1.height, 5)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 0)

    def test_create_square(self):
        """ Test create a Square from a dictionary """
        s1_dictionary = {'id': 2, 'size': 4, 'x': 0, 'y': 2}
        s1 = Square.create(**s1_dictionary)
        self.assertIsInstance(s1, Square)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 2)

    def test_load_from_file_rectangle(self):
        """ Test loading instance of Rectangle from file. """
        filename = "Rectangle.json"
        if os.path.exists(filename):
            os.remvoe(filename)

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        for rect_in, rect_out in zip(list_rectangles_input,
                                     list_rectangles_output):
            self.assertEqual(rect_in.__str(), rect_out.__str__())

        if os.path.exits(filename):
            os.remove(filename)

    def test_load_from_file_square(self):
        """ Test loading instances of Square from file"""
        filename = "Square.json"
        if os.path.exists(filename):
            os.remove(filename)

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        for square_in, square_out in zip(list_squares_input,
                                         list_squares_output):
            self.assertEqual(suqare_in.__str(), square_out.__str__())

        if os.path.exists(filename):
            os.remove(filename)
