import unittest
from .myadd import add


class MyAddTestSuite(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(15, add(10, 5), "should be 15")

    def test_add2(self):
        self.assertEqual(-5, add(-10, 5), "should be -5")

    def test_add3(self):
        self.assertEqual(-15, add(-10, -5), "should be -15")

    def test_add4(self):
        self.assertEqual(4, add(1, 3), "should be 4")


if __name__ == "__main__":
    unittest.main()
