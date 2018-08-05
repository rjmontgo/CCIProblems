import unittest

from problem_6 import isPalindrome
from lib.linkedlist import LinkedList

class TestIsPalindrome(unittest.TestCase):

    def test_one_letter(self):
        l1 = LinkedList()
        l1.add('a')

        self.assertEqual(True, isPalindrome(l1, len(l1), "1"))

    def test_two_letter(self):
        l1 = LinkedList()
        l1.add('a')
        l1.add('b')

        self.assertEqual(False, isPalindrome(l1, len(l1), "2"))

    def test_three_letter(self):
        l1 = LinkedList()
        l1.add('a')
        l1.add('b')
        l1.add('a')

        self.assertEqual(True, isPalindrome(l1, len(l1), "3"))

    def test_four_letter(self):
        l1 = LinkedList()
        l1.add('a')
        l1.add('b')
        l1.add('b')
        l1.add('a')

        self.assertEqual(True, isPalindrome(l1, len(l1), "4"))
