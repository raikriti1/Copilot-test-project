import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.main import greet

class TestMain(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Alice"), "Welcome to the Copilot Python Demo, Alice!")

if __name__ == '__main__':
    unittest.main()