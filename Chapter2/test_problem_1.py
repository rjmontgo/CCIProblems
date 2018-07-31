import unittest
from lib.linkedlist import LinkedList
from problem_1 import removeDups

class TestRemoveDups(unittest.TestCase):

    def helper_equal_lists(self, l1, l2):
        node1 = l1.root
        node2 = l2.root

        if ((not node1 or not node2) or node1.data != node2.data):
            return False

        while (node1.next and node2.next):
            if (not node2) or (node1.data != node2.data):
                return False
            node1 = node1.next
            node2 = node2.next

        return node1.next.data == node2.next.data

    def setUp(self):
        self.l1 = LinkedList()
        self.l2 = LinkedList()

    def test_single_element(self):
        self.l1.add(1)
        self.l2.add(1)

        self.assertEqual(self.helper_equal_lists(removeDups(self.l1), self.l2),
                        True)

    def test_one_dup(self):
        self.l1.add(1)
        self.l1.add(2)
        self.l1.add(2)

        self.l2.add(1)
        self.l2.add(2)

        self.assertEqual(self.helper_equal_lists(removeDups(self.l1), self.l2),
                        True)

if __name__ is '__main__':
    unittest.main()
