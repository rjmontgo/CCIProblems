import unittest

from lib.linkedlist import LinkedList
from problem_5 import addLists

class TestAddLists(unittest.TestCase):

    def test_three_digit(self):
        l1 = LinkedList()
        l2 = LinkedList()

        l1.add(1)
        l1.add(2)
        l1.add(3)

        l2.add(4)
        l2.add(5)
        l2.add(6)

        result = LinkedList()
        result.add(5)
        result.add(7)
        result.add(9)

        self.assertEqual(result, addLists(l1, l2))

    def test_overflow_ones_place(self):
        l1 = LinkedList()
        l2 = LinkedList()

        l1.add(2)
        l1.add(1)
        l1.add(4)

        l2.add(4)
        l2.add(1)
        l2.add(6)

        result = LinkedList()
        result.add(6)
        result.add(3)
        result.add(0)

        self.assertEqual(result, addLists(l1, l2))

    def test_overflow_result_longer(self):
        l1 = LinkedList()
        l2 = LinkedList()

        l1.add(9)
        l1.add(1)
        l1.add(1)

        l2.add(1)
        l2.add(9)
        l2.add(9)

        result = LinkedList()
        result.add(1)
        result.add(1)
        result.add(1)
        result.add(0)

        self.assertEqual(result, addLists(l1, l2))

    def test_long_short_parameters(self):
        l1 = LinkedList()
        l2 = LinkedList()

        l1.add(1)
        l1.add(0)
        l1.add(0)
        l1.add(0)

        l2.add(1)

        result = LinkedList()
        result.add(1)
        result.add(0)
        result.add(0)
        result.add(1)

        self.assertEqual(result, addLists(l1, l2))

    def test_long_parameters_result_overflow(self):
        l1 = LinkedList()
        l2 = LinkedList()

        l1.add(1)
        l1.add(0)
        l1.add(0)
        l1.add(0)

        l2.add(9)
        l2.add(0)
        l2.add(0)
        l2.add(0)

        result = LinkedList()
        result.add(1)
        result.add(0)
        result.add(0)
        result.add(0)
        result.add(0)

        self.assertEqual(result, addLists(l1, l2))
