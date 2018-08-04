import unittest

from lib.linkedlist import LinkedList
from problem_3 import deleteMiddle

class TestDeleteMiddle(unittest.TestCase):

    def test_three_elements(self):
        three_elem = LinkedList()
        three_elem.add(1)
        three_elem.add(2)
        three_elem.add(3)
        node = three_elem.root.next
        deleteMiddle(node)

        result = LinkedList()
        result.add(1)
        result.add(3)

        self.assertEqual(result, three_elem)

    def test_four_elements(self):
        four_elem = LinkedList()
        four_elem.add(1)
        four_elem.add(2)
        four_elem.add(3)
        four_elem.add(4)

        node = four_elem.root.next.next
        deleteMiddle(node)

        result = LinkedList()
        result.add(1)
        result.add(2)
        result.add(4)

        self.assertEqual(result, four_elem)

    def test_different_nums(self):
        diff_nums = LinkedList()
        diff_nums.add(3)
        diff_nums.add(4)
        diff_nums.add(2)
        diff_nums.add(1)
        diff_nums.add(7)

        node = diff_nums.root.next.next
        deleteMiddle(node)

        result = LinkedList()
        result.add(3)
        result.add(4)
        result.add(1)
        result.add(7)
        self.assertEqual(result, diff_nums)
