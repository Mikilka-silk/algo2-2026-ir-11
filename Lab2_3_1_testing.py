import unittest
from Lab2_3_1 import max_hamsters

class HamstersTest(unittest.TestCase):
    def test_case_0(self):
        S = 7
        C = 3
        hamsters = [
            [1, 2],
            [2, 2],
            [3, 1]
        ]
        self.assertEqual(max_hamsters(S, C, hamsters), 2)

    def test_case_2(self):
        S = 19
        C = 4
        hamsters = [
            [5, 0], 
            [2, 2], 
            [1, 4], 
            [5, 1]
        ]
        self.assertEqual(max_hamsters(S, C, hamsters), 3)

    def test_case_3(self):
        S = 2
        C = 2
        hamsters = [
            [1, 50000], 
            [1, 60000]    
        ]
        self.assertEqual(max_hamsters(S, C, hamsters), 1)

    def test_case_zero_food(self):
        S = 0
        C = 2
        hamsters = [
            [1, 2], 
            [2, 2]
        ]
        self.assertEqual(max_hamsters(S, C, hamsters), 0)

    def test_case_can_feed_all(self):
        S = 100
        C = 2
        hamsters = [
            [1, 2], 
            [2, 2]
        ]
        self.assertEqual(max_hamsters(S, C, hamsters), 2)

if __name__ == "__main__":
    unittest.main()
