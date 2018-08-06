import unittest

from problem_3 import SetOfStacks

class TestSetOfStacks(unittest.TestCase):

    def test_push_one(self):
        stack = SetOfStacks()

        stack.push(1)
        self.assertEqual(1, stack.pop())

    def test_push_five(self):
        stack = SetOfStacks()

        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.push(6)
        self.assertEqual(6, stack.pop())

    def test_push_ten(self):

        stack = SetOfStacks()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.push(6)
        stack.push(7)
        stack.push(8)
        stack.push(9)
        stack.push(10)
        stack.push(11)
        stack.push(12)
        self.assertEqual(12, stack.pop())
        self.assertEqual(11, stack.pop())
        self.assertEqual(10, stack.pop())
        self.assertEqual(9, stack.pop())
        self.assertEqual(8, stack.pop())
        self.assertEqual(7, stack.pop())
        self.assertEqual(6, stack.pop())
        self.assertEqual(5, stack.pop())
