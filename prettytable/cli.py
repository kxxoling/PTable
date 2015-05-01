from __future__ import print_function
import argparse
from .factory import from_csv


def main():
    parser = argparse.ArgumentParser(description='A simple Python library designed to make it quick and easy to '
                                     'represent tabular data in visually appealing ASCII tables.')
    parser.add_argument('--csv', help='CSV file name')
    args = parser.parse_args()
    with open(args.csv) as fp:
        print(from_csv(fp))


if __name__ == '__main__':
    main()
