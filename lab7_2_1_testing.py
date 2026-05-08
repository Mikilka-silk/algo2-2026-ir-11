import unittest
from lab7_2_1 import prim_mst 

class TestMST(unittest.TestCase):
    def test_case_0(self):
        matrix = [
            [0, 10, 20],
            [10, 0, 5],
            [20, 5, 0]
        ]
        self.assertEqual(prim_mst(matrix), 15)

    def test_case_1(self):
        self.assertEqual(prim_mst([]), 0)

    def test_case_2(self):
        matrix = [
            [0, 10, 0],
            [10, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(prim_mst(matrix), 10)

if __name__ == '__main__':
    unittest.main()
