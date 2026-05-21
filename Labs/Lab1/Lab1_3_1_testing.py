import unittest
from Lab1_3_1 import zigzag
class ZigZagTest(unittest.TestCase):
    def test_case_0(self):
        wanted_result = [
            [1, 2, 6, 7, 12],
            [3, 5, 8, 11, 13],
            [4, 9, 10, 14, 15]
        ]
        self.assertEqual(zigzag(5, 3), wanted_result)

    def test_case_1(self):
        wanted_result = [
            [1, 2, 6, 7, 15],
            [3, 5, 8, 14, 16],
            [4, 9, 13, 17, 22],
            [10, 12, 18, 21, 23],
            [11, 19, 20, 24, 25]
        ]
        self.assertEqual(zigzag(5, 5), wanted_result)
    
    def test_case_2(self):
        wanted_result = [
            [1, 2, 5, 6],
            [3, 4, 7, 8]
        ]
        self.assertEqual(zigzag(4, 2), wanted_result)

    def test_case_3(self):
        wanted_result = [
            [1], [2], [3], [4], [5], [6],
        ]
        self.assertEqual(zigzag(1, 6), wanted_result)

    def test_case_4(self):
        wanted_result = [
            [1]
            ]
        self.assertEqual(zigzag(1, 1), wanted_result)
if __name__ == "__main__":
    unittest.main()
