import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate("2+2"), 4)
        self.assertEqual(calculate("2.5+2.5"), 5.0)
        self.assertEqual(calculate("-2+2"), 0)

    def test_subtract(self):
        self.assertEqual(calculate("2-2"), 0)
        self.assertEqual(calculate("2.5-2.5"), 0.0)
        self.assertEqual(calculate("-2-2"), -4)

    def test_multiply(self):
        self.assertEqual(calculate("2*2"), 4)
        self.assertEqual(calculate("2.5*2.5"), 6.25)
        self.assertEqual(calculate("-2*2"), -4)

    def test_divide(self):
        self.assertEqual(calculate("2/2"), 1)
        self.assertEqual(calculate("2.5/2.5"), 1.0)
        self.assertEqual(calculate("-2/2"), -1)

    def test_divide_by_zero(self):
        self.assertEqual(calculate("2/0"), "Erro")

    def test_invalid_expression(self):
        self.assertEqual(calculate("2+"), "Erro")
        self.assertEqual(calculate("2++2"), "Erro")

    def test_order_of_operations(self):
        self.assertEqual(calculate("2+2*2"), 6)
        self.assertEqual(calculate("2*2+2"), 6)
        self.assertEqual(calculate("2+2/2"), 3)
        self.assertEqual(calculate("2/2+2"), 3)

    def test_parentheses(self):
        self.assertEqual(calculate("(2+2)*2"), 8)
        self.assertEqual(calculate("2*(2+2)"), 8)
        self.assertEqual(calculate("(2+2)/2"), 2)
        self.assertEqual(calculate("2/(2+2)"), 0.5)

if __name__ == "__main__":
    unittest.main()
