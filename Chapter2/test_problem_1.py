import unittest
from lib.linkedlist import LinkedList
from problem_1 import removeDups

class TestRemoveDups(unittest.TestCase):

    def helper_equal_lists(self, l1, l2):
        node1 = l1.root
        node2 = l2.root

        while node1 and node2:
            if (node1.data != node2.data):
                return False

            node1 = node1.next
            node2 = node2.next

        return not (node1 or node2)

    def setUp(self):
        self.l1 = LinkedList()
        self.l2 = LinkedList()

    def test_single_element(self):
        self.l1.add(1)
        self.l2.add(1)

        self.assertEqual(self.helper_equal_lists(self.l2, removeDups(self.l1)),
                        True)

    def test_one_dup(self):
        self.l1.add(1)
        self.l1.add(2)
        self.l1.add(2)

        self.l2.add(1)
        self.l2.add(2)

        self.assertEqual(self.helper_equal_lists(self.l2, removeDups(self.l1)),
                        True)

    def test_three_dups(self):
        self.l1.add(1)
        self.l1.add(2)
        self.l1.add(2)
        self.l1.add(3)
        self.l1.add(3)

        self.l2.add(1)
        self.l2.add(2)
        self.l2.add(3)

        self.assertEqual(self.helper_equal_lists(self.l2, removeDups(self.l1)),
                        True)

    def test_high_dup_occurence(self):
        self.l1.add(1)
        self.l1.add(2)
        self.l1.add(2)
        self.l1.add(3)
        self.l1.add(3)
        self.l1.add(3)
        self.l1.add(3)

        self.l2.add(1)
        self.l2.add(2)
        self.l2.add(3)

        self.assertEqual(self.helper_equal_lists(self.l2, removeDups(self.l1)),
                        True)

    def test_interspersed_dups(self):
        self.l1.add(1)
        self.l1.add(2)
        self.l1.add(2)
        self.l1.add(3)
        self.l1.add(3)
        self.l1.add(4)
        self.l1.add(4)
        self.l1.add(3)
        self.l1.add(5)
        self.l1.add(5)
        self.l1.add(5)
        self.l1.add(3)
        self.l1.add(2)
        self.l1.add(6)
        self.l1.add(6)

        self.l2.add(1)
        self.l2.add(2)
        self.l2.add(3)
        self.l2.add(4)
        self.l2.add(5)
        self.l2.add(6)

        self.assertEqual(self.helper_equal_lists(self.l2, removeDups(self.l1)),
                        True)

    def test_out_of_order_dups(self):
        self.l1.add(1)
        self.l1.add(3)
        self.l1.add(2)
        self.l1.add(5)
        self.l1.add(2)
        self.l1.add(3)
        self.l1.add(4)
        self.l1.add(4)
        self.l1.add(3)
        self.l1.add(5)
        self.l1.add(5)
        self.l1.add(3)
        self.l1.add(2)
        self.l1.add(6)
        self.l1.add(6)

        self.l2.add(1)
        self.l2.add(3)
        self.l2.add(2)
        self.l2.add(5)
        self.l2.add(4)
        self.l2.add(6)

        self.assertEqual(self.helper_equal_lists(self.l2, removeDups(self.l1)),
                        True)

    def test_invalid_case_dups_in_expected(self):
        self.l1.add(1)
        self.l1.add(3)
        self.l1.add(2)
        self.l1.add(5)
        self.l1.add(2)
        self.l1.add(3)
        self.l1.add(4)
        self.l1.add(4)
        self.l1.add(3)
        self.l1.add(5)
        self.l1.add(5)
        self.l1.add(3)
        self.l1.add(2)
        self.l1.add(6)
        self.l1.add(6)

        self.l2.add(1)
        self.l2.add(3)
        self.l2.add(3)
        self.l2.add(2)
        self.l2.add(5)
        self.l2.add(4)
        self.l2.add(6)

        self.assertEqual(self.helper_equal_lists(self.l2, removeDups(self.l1)),
                        False)

    def test_invalid_case_dups_out_of_order(self):
        self.l1.add(1)
        self.l1.add(3)
        self.l1.add(2)
        self.l1.add(5)
        self.l1.add(2)
        self.l1.add(3)
        self.l1.add(4)
        self.l1.add(4)
        self.l1.add(3)
        self.l1.add(5)
        self.l1.add(5)
        self.l1.add(3)
        self.l1.add(2)
        self.l1.add(6)
        self.l1.add(6)

        self.l2.add(3)
        self.l2.add(1)
        self.l2.add(2)
        self.l2.add(5)
        self.l2.add(4)
        self.l2.add(6)

        self.assertEqual(self.helper_equal_lists(self.l2, removeDups(self.l1)),
                        False)

if __name__ is '__main__':
    unittest.main()
