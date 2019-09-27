import data_viz
import argparse
import get_data as g


def main():
    """main function calling viz"""
    parser = argparse.ArgumentParser(description="type of plot and file name")
    parser.add_argument('out_name', type=str, help='specify output file name')
    parser.add_argument('type', type=str, help='choose type of plot')
    args = parser.parse_args()

    if args.type == 'histogram':
        foo = data_viz.histogram(g.read_stdin_col(0), args.out_name)

    elif args.type == 'boxplot':
        foo = data_viz.boxplot(g.read_stdin_col(0), args.out_name)

    elif args.type == 'combo':
        foo = data_viz.combo(g.read_stdin_col(0), args.out_name)

    else:
        raise ValueError('Choose histogram, boxplot, or combo')


if __name__ == '__main__':
    main()
