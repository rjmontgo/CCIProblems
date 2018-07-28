import unittest

from problem_5 import isOneAway

class TestIsOneAway(unittest.TestCase):

    def test_one_char_add(self):
        self.assertEqual(isOneAway("", "a"), True)

    def test_one_char_remove(self):
        self.assertEqual(isOneAway("a", ""), True)

    def test_one_char_replace(self):
        self.assertEqual(isOneAway("a", "v"), True)

    def test_two_char_add(self):
        self.assertEqual(isOneAway("a", "ab"), True)

    def test_two_char_remove(self):
        self.assertEqual(isOneAway("ab", "a"), True)

    def test_two_char_replace(self):
        self.assertEqual(isOneAway("ac", "ab"), True)

    def test_two_char_away_add(self):
        self.assertEqual(isOneAway("", "aa"), False)

    def test_two_char_away_remove(self):
        self.assertEqual(isOneAway("ab", ""), False)

    def test_two_char_away_replace(self):
        self.assertEqual(isOneAway("av", "cd"), False)



if __name__ is '__main__':
    unittest.main()
