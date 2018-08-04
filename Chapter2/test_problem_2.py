import unittest

from problem_2 import kFromEnd
from lib.linkedlist import LinkedList

class TestKFromEnd(unittest.TestCase):

    def test_empty_list(self):
        l1 = LinkedList()
        self.assertEqual(None, kFromEnd(l1, 0))

    def test_one_element(self):
        l1 = LinkedList()
        l1.add(1)
        self.assertEqual(1, kFromEnd(l1, 0))

    def test_two_elements(self):
        l1 = LinkedList()
        l1.add(1)
        l1.add(2)
        self.assertEqual(1, kFromEnd(l1, 1))

    def test_four_elements(self):
        l1 = LinkedList()
        l1.add(1)
        l1.add(2)
        l1.add(3)
        l1.add(4)

        self.assertEqual(2, kFromEnd(l1, 2))

    def test_large_elements(self):
        l1 = LinkedList()
        l1.add(1)
        l1.add(2)
        l1.add(3)
        l1.add(4)
        l1.add(5)
        l1.add(6)
        l1.add(7)
        l1.add(8)
        l1.add(9)
        l1.add(10)
        l1.add(11)


        self.assertEqual(8, kFromEnd(l1, 3))


if __name__ is '__main__':
    unittest.main()
