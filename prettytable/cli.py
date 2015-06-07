from __future__ import print_function
import argparse
import sys

from .factory import from_csv, from_md
from ._compact import StringIO


def main():
    parser = argparse.ArgumentParser(description='A simple Python library designed to make it quick and easy to '
                                     'represent tabular data in visually appealing ASCII tables.')
    parser.add_argument('--csv', help='CSV file name')
    parser.add_argument('--md', help='Markdown file name')
    parser.add_argument('--rst', help='reStructuredText file name')
    args = parser.parse_args()

    if args.csv:
        with open(args.csv) as fp:
            print(from_csv(fp))
    elif args.md:
        with open(args.md) as md:
            print(from_md(md.read()))
    else:
        text_in = sys.stdin.read()
        print(from_csv(StringIO.StringIO(text_in)))


if __name__ == '__main__':
    main()
