"""
test_quadratic.py - Unit tests for quadratic.py
Run with: python -m unittest tests.test_quadratic   (from the project root)
"""

import unittest
from calculator.quadratic import solve

class TestQuadratic(unittest.TestCase):
    # Test two distinct real roots
    def test_two_real_roots(self):
        self.assertEqual(solve(1, -5, 6), (3.0, 2.0))

    # Test one repeated root
    def test_repeated_root(self):
        self.assertEqual(solve(1, -2, 1), (1.0, 1.0))

    # Test no real roots
    def test_no_real_roots(self):
        self.assertIsNone(solve(1, 2, 5))

    # Test when a = 0
    def test_zero_a_raises(self):
        with self.assertRaises(ValueError):
            solve(0, 2, 3)

if __name__ == "__main__":
    unittest.main()