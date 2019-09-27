import get_data
import math_lib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def boxplot(L, out_file_name):
    """generates boxplot of data"""

    fig_box = plt.figure(figsize=(3, 3), dpi=300)
    boxax = fig_box.add_subplot(1, 1, 1)
    boxax.boxplot(L)
    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)
    boxax.set_title('mean = %s, stdev = %s' % (mean, stdev))
    boxax.set_ylabel('Value')
    fig_box.savefig(out_file_name, bbox_inches='tight')
    plt.close()

    return out_file_name


def histogram(L, out_file_name):
    """generates histogram of data"""

    fig_hist = plt.figure(figsize=(3, 3), dpi=300)
    histax = fig_hist.add_subplot(1, 1, 1)
    histax.hist(L)
    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)
    histax.set_title('mean=%s, stdev=%s' % (mean, stdev))
    histax.set_xlabel('Value')
    histax.set_ylabel('Frequency')
    fig_hist.savefig(out_file_name, bbox_inches='tight')
    plt.close()

    return out_file_name


def combo(L, out_file_name):
    """generates histogram and boxplot of data"""
    fig_c = plt.figure()
    ax1 = fig_c.add_subplot(1, 2, 1)
    ax1.boxplot(L)
    ax1.set_ylabel('Value')

    ax0 = fig_c.add_subplot(1, 2, 2)
    ax0.hist(L)
    ax0.set_xlabel('Value')
    ax0.set_ylabel('Frequency')

    fig_c.tight_layout()
    fig_c.savefig(out_file_name, bbox_inches='tight')
    plt.close()

    return out_file_name
