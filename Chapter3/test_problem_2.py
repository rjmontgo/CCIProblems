import unittest
from problem_2 import *

class TestMinStack(unittest.TestCase):

    def test_one_element_min(self):
        minStack = MinStack()
        minStack.push(1)

        self.assertEqual(1, minStack.min())

    def test_five_element_min(self):
        minStack = MinStack()
        minStack.push(1)
        minStack.push(0)
        minStack.push(2)
        minStack.push(3)
        minStack.push(4)

        self.assertEqual(0, minStack.min())

    def test_popping_min(self):
        minStack = MinStack()
        minStack.push(1)
        minStack.push(0)
        minStack.push(2)
        minStack.push(3)
        minStack.push(-2)
        minStack.pop()
        self.assertEqual(0, minStack.min())

    def test_popping_min_multiple_times(self):
        minStack = MinStack()
        minStack.push(1)
        minStack.push(2)
        minStack.push(-1)
        minStack.push(-2)

        self.assertEqual(-2, minStack.min())

        minStack.pop()

        self.assertEqual(-1, minStack.min())

        minStack.pop()

        self.assertEqual(1, minStack.min())


if __name__ is '__main__':
    unittest.main()
