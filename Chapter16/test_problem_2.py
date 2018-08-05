import unittest

from problem_2 import processBook, numOccurences

class TestNumOccurences(unittest.TestCase):

    def test_string(self):
        fileroute = "mockdata/string.txt"
        map = processBook(fileroute)
        self.assertEqual(2, numOccurences(map, "test"))
        self.assertEqual(1, numOccurences(map, "testo"))
        self.assertEqual(1, numOccurences(map, "dog"))

    def test_small_page(self):
        fileroute = "mockdata/loremipsum.txt"
        map = processBook(fileroute)
        self.assertEqual(3, numOccurences(map, "sit"))
        self.assertEqual(4, numOccurences(map, "ut"))
        self.assertEqual(4, numOccurences(map, "qui"))

    def test_whole_book(self):
        fileroute = "mockdata/mobydick.txt"
        map = processBook(fileroute)
        self.assertEqual(495, numOccurences(map, "whale"))
        self.assertEqual(14, numOccurences(map, "elijah"))
        self.assertEqual(32, numOccurences(map, "harpoon"))

if __name__ is '__main__':
    unittest.main()
