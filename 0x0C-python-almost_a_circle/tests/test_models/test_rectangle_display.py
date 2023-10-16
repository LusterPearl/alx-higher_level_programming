import unnittest
from io import StringIO
import sys
from models.rectangle import Rectangle


class TestRectangleDisplay(unittest.TestCase):
    def test_display(self):
        r1 = Rectangle(2, 3, 2, 2,)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        expected_outpu = "  ##\n  ##\n  ##\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
