import unittest
from problem_8 import zeroMatrix

class TestZeroMatrix(unittest.TestCase):

    def test_empty_matrix(self):
        self.assertEqual(zeroMatrix([[]]), [[]])

    def test_one_element_matrix(self):
        self.assertEqual(zeroMatrix([[1]]), [[1]])

    def test_two_by_two_matrix(self):
        self.assertEqual(zeroMatrix([
            [1, 2],
            [3, 0]
            ]), [
            [1, 0],
            [0, 0]
            ])

    def test_two_by_three_one_zero(self):
        self.assertEqual(zeroMatrix([
            [1, 0, 2],
            [3, 4, 5],
            ]),[
            [0, 0, 0],
            [3, 0, 5]
            ])

    def test_two_by_three_two_zeroes(self):
        self.assertEqual(zeroMatrix([
            [0, 0, 3],
            [2, 1, 4]
            ]), [
            [0, 0, 0],
            [0, 0, 4]
            ])

    def test_three_by_three(self):
        self.assertEqual(zeroMatrix([
            [2, 1, 2],
            [0, 4, 0],
            [6, 7, 0]
            ]),[
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0]
            ])

    def test_all_zeroes(self):
        self.assertEqual(zeroMatrix([
            [0, 0],
            [0, 0]
            ]),[
            [0, 0],
            [0, 0]
            ])

    def test_no_zeroes(self):
        self.assertEqual(zeroMatrix([
            [1, 2],
            [3, 4]
            ]), [
            [1, 2],
            [3, 4]
            ])



if __name__ is '__main__':
    unittest.main()
