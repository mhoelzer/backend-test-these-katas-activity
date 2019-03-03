import unittest
from katas import add, multiply, power, factorial, fibonacci


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 2), 5)
        # self.assertEqual(add(3, 3), 5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)
        # self.assertEqual(multiply(2, 6), 8)

    def test_power(self):
        self.assertEqual(power(3, 4), 81)
        # self.assertEqual(power(3, 3), 81)

    def test_factorial(self):
        self.assertEqual(factorial(4), 24)
        # self.assertEqual(factorial(4), 25)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(8), 13)
        # self.assertEqual(fibonacci(8), 21)


if __name__ == '__main__':
    unittest.main()
