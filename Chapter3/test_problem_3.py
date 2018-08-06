import unittest

from problem_3 import SetOfStacks

class TestSetOfStacks(unittest.TestCase):

    def test_push_one():
        stack = SetOfStacks()

        stack.push(1)
        self.assertEqual(1, stack.pop())

    def test_push_five():
        stack = SetOfStacks()

        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.push(6)
        self.assertEqual(6, stack.pop())

    
