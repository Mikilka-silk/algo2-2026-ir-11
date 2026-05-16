import unittest
from lab8_2_1 import count_paths

class TestIJones(unittest.TestCase):

    def test_case_0(self):
        W, H = 3, 3
        grid = [
            "aaa",
            "cab",
            "def"
        ]
        self.assertEqual(count_paths(W, H, grid), 5)

    def test_case_1(self):
        W, H = 10, 1
        grid = [
            "abcdefaghi"
        ]
        self.assertEqual(count_paths(W, H, grid), 2)

    def test_case_2(self):
        W, H = 7, 6
        grid = [
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa"
        ]
        self.assertEqual(count_paths(W, H, grid), 201684)

    def test_case_3(self):
        W, H = 3, 2
        grid = [
            "abc",
            "def"
        ]
        self.assertEqual(count_paths(W, H, grid), 2)

    def test_case_4(self):
        W, H = 4, 1
        grid = [
            "abab"
        ]
        self.assertEqual(count_paths(W, H, grid), 3)

    def test_case_5(self):
        W, H = 4, 3
        grid = [
            "abaa",
            "caca",
            "dddd"
        ]
        self.assertEqual(count_paths(W, H, grid), 11)

if __name__ == "__main__":
    unittest.main()