import unittest
import data_viz
import os.path
import os
import get_data as g
from os import path


class TestDataVizBox(unittest.TestCase):
    """testing histogram creation function"""

    def test_file_not_there_originally_box(self):
        """test file not there before generation"""
        self.assertFalse(path.exists("./box.png"))

    def test_file_there_afterward_box(self):
        """test there after generation"""
        r = data_viz.boxplot(g.read_stdin_col(0), 'box.png')
        self.assertTrue(path.exists("./box.png"))


if __name__ == '__main__':
    if path.exists("./box.png") is True:
        os.remove('./box.png')

    unittest.main()
