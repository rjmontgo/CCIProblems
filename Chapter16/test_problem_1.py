import unittest

from problem_1 import inPlaceSwap

class TestInPlaceSwap(unittest.TestCase):

    def test_swapping_two_ints(self):
        arr = [1, 2]
        self.assertEqual([2, 1], inPlaceSwap(arr))

    def test_swapping_two_more_ints(self):
        arr = [31, 23]
        self.assertEqual([23, 31], inPlaceSwap(arr))

if __name__ is '__main__':
    unittest.main()
