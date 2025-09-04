import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.utils.helpers import calculate, format_data

class TestHelpers(unittest.TestCase):

    def test_calculate(self):
        self.assertEqual(calculate(2, 3), 5)
        self.assertEqual(calculate(-1, 1), 0)
        self.assertEqual(calculate(0, 0), 0)

    def test_format_data(self):
        self.assertEqual(format_data("test"), "Test")
        self.assertEqual(format_data("HELLO"), "Hello")
        self.assertEqual(format_data(""), "") 

if __name__ == '__main__':
    unittest.main()