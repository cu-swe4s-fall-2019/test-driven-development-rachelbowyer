import unittest
import math_lib
import random
import statistics as stat
import math as m


class TestMathLib(unittest.TestCase):
    """tests of the module math lib"""
    def test_list_mean_none(self):
        """test for if list_mean is passed None"""
        r = math_lib.list_mean(None)
        self.assertEqual(r, None)


    def test_list_mean_empty_list(self):
        """test for if list_mean is passed empty list"""
        r = math_lib.list_mean([])
        self.assertEqual(r, None)


    def test_list_mean_constants(self):
        """test for mean of constant list"""
        r = math_lib.list_mean([1, 1, 1, 1])
        self.assertEqual(r, 1)


if __name__ == '__main__':
    unittest.main()