import unittest
from models.rectangle import Rectangle

class TestRectangleValidation(unittest.TestCase):
    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 10)
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 10)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, "invalid")
        with self.assertRaies(ValueError):
            r = Rectangle(10, -10)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 10, "invalid")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 10, -1)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 10, 0, "invalid")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 10, 0, -1)

if __name__ == '__main__:
    unittest.main()
