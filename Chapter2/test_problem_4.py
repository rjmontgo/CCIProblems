import unittest

from lib.linkedlist import LinkedList
from problem_4 import partitionList

class TestPartitionList(unittest.TestCase):

    def test_partition_sorted_list(self):
        l1 = LinkedList()
        result = LinkedList()

        result.add(1)
        result.add(4)
        result.add(3)
        result.add(2)

        l1.add(1)
        l1.add(2)
        l1.add(3)
        l1.add(4)

        self.assertEqual(result, partitionList(l1, 2))

    def test_partition_four_elem(self):
        l1 = LinkedList()
        result = LinkedList()

        result.add(2)
        result.add(1)
        result.add(4)
        result.add(3)

        l1.add(1)
        l1.add(3)
        l1.add(4)
        l1.add(2)

        self.assertEqual(result, partitionList(l1, 3))

    def test_large_elements(self):
        l1 = LinkedList()
        result = LinkedList()

        l1.add(2)
        l1.add(9)
        l1.add(7)
        l1.add(6)
        l1.add(3)
        l1.add(4)
        l1.add(1)

        result.add(1)
        result.add(3)
        result.add(2)
        result.add(4)
        result.add(6)
        result.add(7)
        result.add(9)

        self.assertEqual(result, partitionList(l1, 4))


if __name__ is '__main__':
    unittest.main()
