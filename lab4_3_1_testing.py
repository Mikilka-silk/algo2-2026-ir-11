import unittest
from lab4_3_1 import RBPriorityQueue

class TestRBPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = RBPriorityQueue()
        
        self.pq.insert("Task 1 (Mid)", 10)
        self.pq.insert("Task 2 (High)", 20)
        self.pq.insert("Task 3 (Low)", 5)
        self.pq.insert("Task 4 (Mid)", 10)
        self.pq.insert("Task 5 (Very High)", 50)

    def test_case_0(self):
        val, prio = self.pq.peek()
        self.assertEqual(prio, 50)
        self.assertEqual(val, "Task 5 (Very High)")

    def test_case_1(self):
        val, prio = self.pq.extract_max()
        self.assertEqual(prio, 50)
        
        next_val, next_prio = self.pq.peek()
        self.assertEqual(next_prio, 20)

    def test_case_2(self):
        self.pq.extract_max() 
        val, prio = self.pq.extract_max()
        self.assertEqual(prio, 20)
        self.assertEqual(val, "Task 2 (High)")

    def test_case_3(self):
        self.pq.extract_max()
        self.pq.extract_max()
         
        val1, prio1 = self.pq.extract_max()
        self.assertEqual(prio1, 10)
        val2, prio2 = self.pq.extract_max()
        self.assertEqual(prio2, 10)

    def test_case_4(self):
        self.pq.insert("Task 6 (Ultra High)", 100)
        val, prio = self.pq.extract_max()
        self.assertEqual(prio, 100)
        self.assertEqual(val, "Task 6 (Ultra High)")

    def test_case_5(self):
        self.pq.extract_max() 
        self.pq.extract_max() 
        self.pq.extract_max() 
        self.pq.extract_max() 
        self.pq.extract_max() 
        
        result = self.pq.extract_max()
        self.assertIsNone(result)

        result_peek = self.pq.peek()
        self.assertIsNone(result_peek)

if __name__ == "__main__":
    unittest.main()
