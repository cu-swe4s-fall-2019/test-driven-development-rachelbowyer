import sys
import numpy as np


def read_stdin_col(col_num):
    """function reads data from stdin and give a column"""
    X = []
    Y = []
    for l in sys.stdin:
        A = l.rstrip().split()
        X.append(float(A[0]))
        Y.append(float(A[1]))
    XY_arr = np.zeros((len(X), 2))  # convert to array
    XY_arr[:, 0] = X
    XY_arr[:, 1] = Y
    return XY_arr[:, col_num]
