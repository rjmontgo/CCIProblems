import unittest

from problem_3 import urlify

class TestURLify(unittest.TestCase):

    def test_no_spaces(self):
        self.assertEqual(urlify("Test"), "Test")

    def test_one_spaces(self):
        self.assertEqual(urlify("Test Test"), "Test%20Test")

    def test_two_spaces(self):
        self.assertEqual(urlify("T st T st"), "T%20st%20T%20st")

    def test_all_spaces(self):
        self.assertEqual(urlify("    "), "%20%20%20%20")


if __name__ is '__main__':
    unittest.main()
