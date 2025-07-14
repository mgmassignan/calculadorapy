import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_add_positive_and_negative_numbers(self):
        self.assertEqual(add(5, -3), 2)

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-10, -4), -6)

    def test_subtract_positive_and_negative_numbers(self):
        self.assertEqual(subtract(10, -4), 14)

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(5, 3), 15)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-5, -3), 15)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(10, 0), 0)

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_divide_float_result(self):
        self.assertEqual(divide(10, 4), 2.5)

# ESSA PARTE AQUI FAZ ELE RODAR NO TERMINAL
if __name__ == '__main__':
    unittest.main()
