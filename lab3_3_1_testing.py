import unittest
from lab3_3_1 import BinaryTree


class FindSuccessorTest(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(10)
        self.node_5 = BinaryTree(5, parent=self.root)
        self.node_15 = BinaryTree(15, parent=self.root)
        self.node_3 = BinaryTree(3, parent=self.node_5)
        self.node_7 = BinaryTree(7, parent=self.node_5)
        self.node_20 = BinaryTree(20, parent=self.node_15)
        self.node_12 = BinaryTree(12, parent=self.node_20)

        self.root.set_left(self.node_5)
        self.root.set_right(self.node_15)

        self.node_5.set_left(self.node_3)
        self.node_5.set_right(self.node_7)

        self.node_15.set_right(self.node_20)
        self.node_20.set_left(self.node_12)

    def test_case_0(self):
        successor = self.node_5.find_successor()
        self.assertEqual(successor, self.node_7)

    def test_case_1(self):
        successor = self.node_7.find_successor()
        self.assertEqual(successor, self.root)

    def test_case_2(self):
        successor = self.node_3.find_successor()
        self.assertEqual(successor, self.node_5)

    def test_case_3(self):
        successor = self.node_15.find_successor()
        self.assertEqual(successor, self.node_12)

    def test_case_4(self):
        successor = self.node_12.find_successor()
        self.assertEqual(successor, self.node_20)

    def test_case_5(self):
        successor = self.node_20.find_successor()
        self.assertIsNone(successor)


if __name__ == "__main__":
    unittest.main()
    
