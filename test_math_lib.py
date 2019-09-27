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
        self.assertEqual(r,None)

        
if __name__ == '__main__':
    unittest.main()