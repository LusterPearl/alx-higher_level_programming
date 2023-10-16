import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangleStr(unittest.TestCase):
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        print(r1)
        print(r2)
        sys.stdout = sys.__stdout__
        expected_output = (
                            "[Rectangle] (12) 2/1 - 4/6\n"
                            "[Rectangle] (1) 1/0 - 5/5\n"
                            )
        self.assertEqual(captured_output.getvalue(), expected_output)
