import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square_constructor(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_square_str(self):
        s = Square(3, 1, 2, 4)
        self.assertEqual(str(s), "[Square] (4) 1/2 - 3")

    def test_square_size_setter(self):
        s = Square(3)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_square_size_validation(self):
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = -1

    def test_square_update_with_args(self):
        s = Square(5)
        s.update(10, 2, 3)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)

    def test_square_update_with_kwargs(self):
        s = Sqaure(5)
        s.update(size=7, x=2)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 2)

    def test_to_dictionary(self):
        r = Square(5, 2, 1)
        expected_dict = {
            'id': 1,
            'size': 5,
            'x': 2,
            'y': 1,
        }
        self.assertEqual(s.to_dictionary(), expected_dict)
