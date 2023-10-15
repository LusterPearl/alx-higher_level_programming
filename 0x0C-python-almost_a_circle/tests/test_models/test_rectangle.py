import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle+attributes(self):
        r = Rectangle(5, 10, 1, 2, 42)
        self.assertEqual(r.id, 42)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEual(r.y, 2)

    def test_rectangle_setters(self):
        r = Rectangle(5, 10)
        r.width = 7
        r.height = 15
        r.x = 3
        r.y = 4
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_validators(self):
        with self.assertRaise(ValueError):
            r = Rectangle(0, 10)
        with self.assertRaises(TypeError):
           r = Rectangle("width", 10)

if __name__ == '__main':
    unittest.main()
