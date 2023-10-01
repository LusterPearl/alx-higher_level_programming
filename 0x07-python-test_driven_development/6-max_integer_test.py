# This is the content of 6-max_integer_test.py
#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Test case 2: List of mixed positive and negative integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test case 2: List of mixed positive and negative integers
        self.assertEqual(max_integer([1, 3, 4, 2, -5, -1]), 4)

        # Test case 3: List of negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test case 4: Empty list
        slef.assertIsNone(max_integer([]))

        # Test case 5: List with a single element
        slef.assertEqual(max_integer([42]), 42)

if __name__ == '__main__':
    unittest.main()
