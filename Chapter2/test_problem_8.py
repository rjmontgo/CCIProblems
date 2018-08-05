import unittest

from lib.linkedlist import LinkedList
from problem_8 import findCycleStart

class TestFindCycleStart(unittest.TestCase):

    def test_no_cycle(self):
        l1 = LinkedList()
        l1.add(1)
        l1.add(2)
        l1.add(3)
        l1.add(4)

        self.assertEqual(None, findCycleStart(l1))

    def test_cycle(self):
        l1 = LinkedList()
        l1.add(1)
        l1.add(2)
        l1.add(3)
        l1.add(4)

        l1.root.next.next.next.next = l1.root.next

        #self.assertEqual(l1.root.next, findCycleStart(l1))


    def test_cycle_immediately(self):
        l1 = LinkedList()
        l1.add(1)
        l1.add(2)
        l1.add(3)
        l1.add(4)

        l1.root.next.next.next.next = l1.root

        #self.assertEqual(l1.root, findCycleStart(l1))

if __name__ is '__main__':
    unittest.main()
