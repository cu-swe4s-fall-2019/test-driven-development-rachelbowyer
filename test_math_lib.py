import unittest
import math_lib
import random
import statistics as stat
import math as m


class TestMathLibMean(unittest.TestCase):
    """tests of the mean ftn in module math lib"""
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

    def test_list_mean_rand_ints(self):
        """test for mean of int list"""
        L = []
        for i in range(100):
            for j in range(10):
                L.append(random.randint(0, 100))
            r = math_lib.list_mean(L)
            e = stat.mean(L)
            self.assertEqual(r, e)

    def test_list_mean_rand_floats(self):
        """test for mean of float list"""
        L = []
        for i in range(100):
            for j in range(10):
                L.append(random.uniform(0, 100))
            r = math_lib.list_mean(L)
            e = stat.mean(L)
            self.assertTrue(m.isclose(r, e))

    def test_list_mean_non_real_number_in_list(self):
        """test if list has bad inputs"""
        L = []
        for i in range(10):
            L.append(random.randint(0, 100))
        L.append('x')

        with self.assertRaises(ValueError) as ex:
            math_lib.list_mean(L)


class TestMathLibStdev(unittest.TestCase):
    """tests of the stdev ftn in module math lib"""

    def test_list_stdev_none(self):
        """test for if list_stdev is passed None"""
        r = math_lib.list_stdev(None)
        self.assertEqual(r, None)

    def test_list_stdev_empty_list(self):
        """test for if list_stdev is passed empty list"""
        r = math_lib.list_stdev([])
        self.assertEqual(r, None)

    def test_list_stdev_constants(self):
        """test for stdev of constant list"""
        r = math_lib.list_stdev([1, 1, 1, 1])
        self.assertEqual(r, 0)

    def test_list_stdev_rand_ints(self):
        """test for stdev of int list"""
        L = []
        for i in range(100):
            for j in range(10):
                L.append(random.randint(0, 100))
            r = math_lib.list_stdev(L)
            e = stat.stdev(L)
            self.assertTrue(m.isclose(r, e))


if __name__ == '__main__':
    unittest.main()
