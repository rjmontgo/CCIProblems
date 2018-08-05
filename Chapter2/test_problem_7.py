import unittest

from lib.linkedlist import LinkedList
from problem_7 import linkIntersection

class TestlinkIntersection(unittest.TestCase):

    def test_same_length(self):
        l1 = LinkedList()
        l2 = LinkedList()

        l1.add(1)
        l1.add(3)
        l1.add(4)
        l2.add('a')

        l2.root.next = l1.root.next

        self.assertEqual(l2.root.next, linkIntersection(l1, l2))

    def test_different_length(self):
        l1 = LinkedList()
        l2 = LinkedList()

        l1.add(1)
        l1.add(2)
        l1.add(3)
        l1.add(4)
        l2.add('a')
        l2.root.next = l1.root.next.next

        self.assertEqual(l2.root.next, linkIntersection(l1, l2))

    def test_end_node_intersection(self):
        l1 = LinkedList()
        l2 = LinkedList()

        l1.add(1)
        l1.add(2)
        l1.add('c')
        l2.add('a')
        l2.add('b')
        l2.root.next.next = l1.root.next.next

        self.assertEqual(l2.root.next.next, linkIntersection(l1, l2))

    def test_same_linked_list(self):
        l1 = LinkedList()
        l2 = LinkedList()

        l1.add(1)
        l1.add(2)
        l1.add(3)

        l2.root = l1.root

        self.assertEqual(l2.root, linkIntersection(l1, l2))

    def test_different_list(self):
        l1 = LinkedList()
        l2 = LinkedList()

        l1.add(1)
        l1.add(2)
        l1.add(3)

        l2.add(1)
        l2.add(2)
        l2.add(3)

        self.assertEqual(None, linkIntersection(l1, l2))

if __name__ is '__main__':
    unittest.main()
