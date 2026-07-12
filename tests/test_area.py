"""
test_area.py - Unit tests for Area.py
Run with: python -m unittest test_area.py
"""

import unittest
import math
from calculator.area import square_area, rectangle_area, circle_area, triangle_area


class TestAreaSquare(unittest.TestCase):
    def test_positive_side(self):
        self.assertEqual(square_area(4), 16)

    def test_zero(self):
        self.assertEqual(square_area(0), 0)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            square_area(-3)


class TestAreaRectangle(unittest.TestCase):
    def test_positive_dimensions(self):
        self.assertEqual(rectangle_area(4, 5), 20)

    def test_zero(self):
        self.assertEqual(rectangle_area(0, 5), 0)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            rectangle_area(-4, 5)
        with self.assertRaises(ValueError):
            rectangle_area(4, -5)
        with self.assertRaises(ValueError):
            rectangle_area(-4, -5)


class TestAreaCircle(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(circle_area(2), math.pi * 4)

    def test_zero_radius(self):
        self.assertEqual(circle_area(0), 0)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            circle_area(-1)


class TestAreaTriangle(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(triangle_area(6, 4), 12)

    def test_zero(self):
        self.assertEqual(triangle_area(0, 4), 0)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            triangle_area(-6, 4)
        with self.assertRaises(ValueError):
            triangle_area(6, -4)


if __name__ == "__main__": 
    unittest.main()