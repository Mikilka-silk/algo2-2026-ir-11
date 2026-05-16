import unittest
from lab9_3_1 import search_finite


class TestFiniteAutomaton(unittest.TestCase):
    def test_case_0(self):
        haystack = "hello world"
        needle = "world"
        self.assertEqual(search_finite(haystack, needle), [6])

    def test_case_1(self):
        haystack = "ababcababcabc"
        needle = "ababc"
        self.assertEqual(search_finite(haystack, needle), [0, 5])

    def test_case_2(self):
        haystack = "this is a test"
        needle = "python"
        self.assertEqual(search_finite(haystack, needle), [])

    def test_case_3(self):
        haystack = "aaaaa"
        needle = "aa"
        self.assertEqual(search_finite(haystack, needle), [0, 1, 2, 3])

    def test_case_4(self):
        self.assertEqual(search_finite("some text", ""), [])
        self.assertEqual(search_finite("", "needle"), [])

    def test_case_5(self):
        haystack = "абабагаламага аба"
        needle = "аба"
        self.assertEqual(search_finite(haystack, needle), [0, 2, 14])


if __name__ == "__main__":
    unittest.main()