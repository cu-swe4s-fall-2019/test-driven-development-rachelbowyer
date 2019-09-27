import unittest
import data_viz
import os.path
import os
import get_data as g
from os import path


class TestDataVizHist(unittest.TestCase):
    """testing histogram creation function"""

    def test_file_not_there_originally_hist(self):
        """test file not there before generation"""
        self.assertFalse(path.exists("./hist.png"))

    def test_file_there_afterward_hist(self):
        """test there after generation"""
        r = data_viz.histogram(g.read_stdin_col(0), 'hist.png')
        self.assertTrue(path.exists("./hist.png"))


if __name__ == '__main__':
    if path.exists("./hist.png") is True:
        os.remove('./hist.png')

    unittest.main()
