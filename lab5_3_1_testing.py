import unittest
import copy
import os
import tempfile
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lab5_3_1 import flood_fill, parse_input, write_output


class TestFloodFillCaseOne(unittest.TestCase):

    def test_case_0(self):
        """Заміна 'X' на 'C' з точки (3, 9)"""
        grid = [
            ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ]
        expected = [
            ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'C', 'C', 'C'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'C', 'C', 'C'],
            ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'C'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'C', 'C', 'C'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'C', 'C', 'C'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'C'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'C', 'C', 'C'],
            ['W', 'B', 'B', 'C', 'B', 'B', 'B', 'B', 'C', 'C'],
            ['W', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
        ]
        result = flood_fill(grid, 3, 9, 'C')
        self.assertEqual(result, expected)

    def test_case_1(self):
        """Матриця з однієї клітинки (заміна самої себе)"""
        grid = [['A']]
        result = flood_fill(grid, 0, 0, 'Z')
        self.assertEqual(result, [['Z']])

    def test_case_2(self):
        """Вся матриця одного кольору (всі клітинки замінюються)"""
        grid = [
            ['A', 'A', 'A'],
            ['A', 'A', 'A'],
            ['A', 'A', 'A'],
        ]
        result = flood_fill(grid, 1, 1, 'B')
        expected = [['B'] * 3 for _ in range(3)]
        self.assertEqual(result, expected)

    def test_case_3(self):
        """Якщо колір заміни збігається з цільовим (матриця не змінюється)"""
        grid = [
            ['A', 'A'],
            ['A', 'B'],
        ]
        original = copy.deepcopy(grid)
        result = flood_fill(grid, 0, 0, 'A')
        self.assertEqual(result, original)

    def test_case_4(self):
        """Заміна ізольованої області не впливає на решту"""
        grid = [
            ['A', 'B', 'A'],
            ['B', 'B', 'B'],
            ['A', 'B', 'A'],
        ]
        result = flood_fill(grid, 0, 0, 'Z')
        self.assertEqual(result[0][0], 'Z')
        self.assertEqual(result[0][2], 'A')
        self.assertEqual(result[2][0], 'A')
        self.assertEqual(result[2][2], 'A')
        self.assertEqual(result[1][1], 'B')

    def test_case_5(self):
        """Початок з кутової клітинки"""
        grid = [
            ['R', 'R', 'G'],
            ['R', 'G', 'G'],
            ['G', 'G', 'G'],
        ]
        result = flood_fill(grid, 0, 0, 'W')
        self.assertEqual(result[0][0], 'W')
        self.assertEqual(result[0][1], 'W')
        self.assertEqual(result[1][0], 'W')
        self.assertEqual(result[0][2], 'G')

    def test_case_6(self):
        """Матриця 2×2"""
        grid = [
            ['X', 'X'],
            ['X', 'Y'],
        ]
        result = flood_fill(grid, 0, 0, 'Z')
        self.assertEqual(result[0][0], 'Z')
        self.assertEqual(result[0][1], 'Z')
        self.assertEqual(result[1][0], 'Z')
        self.assertEqual(result[1][1], 'Y')

    def test_case_7(self):
        """По горизонталі (заміна лише по рядку)"""
        grid = [
            ['A', 'A', 'A', 'A'],
            ['B', 'B', 'B', 'B'],
            ['A', 'A', 'A', 'A'],
        ]
        result = flood_fill(grid, 0, 0, 'C')
        self.assertEqual(result[0], ['C', 'C', 'C', 'C'])
        self.assertEqual(result[1], ['B', 'B', 'B', 'B'])
        self.assertEqual(result[2], ['A', 'A', 'A', 'A'])

    def test_case_8(self):
        """По вертикалі (заміна лише по стовпцю)"""
        grid = [
            ['A', 'B', 'A'],
            ['A', 'B', 'A'],
            ['A', 'B', 'A'],
        ]
        result = flood_fill(grid, 0, 1, 'Z')
        for r in range(3):
            self.assertEqual(result[r][1], 'Z')
            self.assertEqual(result[r][0], 'A')
            self.assertEqual(result[r][2], 'A')

    def test_does_not_modify_original_colors_outside_region(self):
        """Кольори поза зв'язною областю залишаються незмінними"""
        grid = [
            ['R', 'G', 'B'],
            ['G', 'G', 'G'],
            ['B', 'G', 'R'],
        ]
        result = flood_fill(grid, 0, 0, 'W')
        self.assertEqual(result[0][0], 'W')
        self.assertEqual(result[0][2], 'B')
        self.assertEqual(result[2][0], 'B')
        self.assertEqual(result[2][2], 'R')


class TestFloodFillCaseTwo(unittest.TestCase):
    """Тести введення/виведення через файли"""

    def _make_input_file(self, content: str) -> str:
        """Створює тимчасовий input-файл і повертає його шлях"""
        tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8')
        tmp.write(content)
        tmp.close()
        return tmp.name

    def test_parse_input_basic(self):
        """Перевірка коректного парсингу вхідного файлу"""
        content = (
            "3,3\n"
            "0,0\n"
            "'Z'\n"
            "['A', 'B', 'A']\n"
            "['A', 'A', 'B']\n"
            "['B', 'A', 'A']\n"
        )
        path = self._make_input_file(content)
        try:
            grid, row, col, replacement, height, width = parse_input(path)
            self.assertEqual(row, 0)
            self.assertEqual(col, 0)
            self.assertEqual(replacement, 'Z')
            self.assertEqual(height, 3)
            self.assertEqual(width, 3)
            self.assertEqual(grid[0], ['A', 'B', 'A'])
            self.assertEqual(grid[1], ['A', 'A', 'B'])
            self.assertEqual(grid[2], ['B', 'A', 'A'])
        finally:
            os.unlink(path)

    def test_write_output(self):
        """Перевірка запису результату у файл"""
        grid = [['A', 'B'], ['C', 'D']]
        tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.txt',
                                         delete=False, encoding='utf-8')
        tmp.close()
        try:
            write_output(tmp.name, grid)
            with open(tmp.name, encoding='utf-8') as f:
                lines = f.readlines()
            self.assertEqual(len(lines), 2)
            self.assertIn('A', lines[0])
            self.assertIn('B', lines[0])
        finally:
            os.unlink(tmp.name)

    def test_full_pipeline(self):
        """Повний цикл (запис у файл -> parse -> flood_fill -> write -> перевірка)"""
        content = (
            "3,3\n"
            "1,1\n"
            "'Z'\n"
            "['A', 'A', 'A']\n"
            "['A', 'A', 'A']\n"
            "['A', 'A', 'A']\n"
        )
        in_path = self._make_input_file(content)
        out_fd, out_path = tempfile.mkstemp(suffix='.txt')
        os.close(out_fd)
        try:
            grid, row, col, replacement, _, _ = parse_input(in_path)
            result = flood_fill(grid, row, col, replacement)
            write_output(out_path, result)
            with open(out_path, encoding='utf-8') as f:
                lines = [l.strip() for l in f.readlines()]
            self.assertEqual(len(lines), 3)
            for line in lines:
                self.assertIn('Z', line)
                self.assertNotIn('A', line)
        finally:
            os.unlink(in_path)
            os.unlink(out_path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
