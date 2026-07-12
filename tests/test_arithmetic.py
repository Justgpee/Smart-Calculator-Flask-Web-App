import unittest
from calculator.arithmetic import add, subtract, multiply, divide

class TestArithmetic(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_add_decimal_numbers(self):
        self.assertEqual(add(2.5, 1.5), 4.0)

# Subtraction
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(6, 4), 2)
        self.assertEqual(subtract(10, -6), 16)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -2), -3)

    def test_subtract_decimal_numbers(self):
        self.assertEqual(subtract(3.40, 1.29), 2.11)

# Multiplication
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)

    def test_multiply_decimal_numbers(self):
        self.assertEqual(multiply(2.5, 4.0), 10.00)

# Division
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(6, 0), "Cannot divide by zero.")

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-6, -3), 2)

    def test_divide_decimal_numbers(self):
        self.assertEqual(divide(11.0, 2.0), 5.5)


if __name__ == "__main__": 
    unittest.main()