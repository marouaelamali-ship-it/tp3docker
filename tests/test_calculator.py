import unittest
from app.calculator import addition, multiplication

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(-1, 1), -1)
        self.assertEqual(multiplication(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
