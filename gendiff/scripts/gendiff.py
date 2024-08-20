#!/usr/bin/env python3
# script: gendiff.py
import argparse
import gendiff.format
from gendiff.generate import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', default='stylish', help='set format of output'
        )
    args = parser.parse_args()
    path_to_file1 = args.first_file
    path_to_file2 = args.second_file
    data_format = args.format
    f = getattr(gendiff.format, data_format)
    diff = generate_diff(path_to_file1, path_to_file2, f)
    print(diff)


if __name__ == '__main__':
    main()
