import unittest

from problem_4 import QueueStack

class TestQueueStack(unittest.TestCase):

    def test_add_and_remove_one(self):
        queue = QueueStack()
        queue.add(1)
        self.assertEqual(queue.dequeue(), 1)

    def test_add_and_remove_two(self):
        queue = QueueStack()
        queue.add(1)
        queue.add(2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)

    def test_add_and_remove_three(self):
        queue = QueueStack()
        queue.add(1)
        queue.add(2)
        self.assertEqual(queue.dequeue(), 1)
        queue.add(3)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)

if __name__ is '__main__':
    unittest.main()
