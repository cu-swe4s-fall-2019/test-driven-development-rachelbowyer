import unittest
import data_viz
import os.path
import os
import get_data as g
from os import path


class TestDataVizCombo(unittest.TestCase):
    """testing combo plot creation function"""

    def test_file_not_there_originally_combo(self):
        """test file not there before generation"""
        self.assertFalse(path.exists("combo.png"))

    def test_file_there_afterward_combo(self):
        """test there after generation"""
        r = data_viz.combo(g.read_stdin_col(0), 'combo.png')
        self.assertTrue(path.exists("combo.png"))


if __name__ == '__main__':
    if path.exists('./combo.png') is True:
        os.remove('./combo.png')

    unittest.main()
