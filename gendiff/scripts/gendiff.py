#!/usr/bin/env python3
# script: gendiff.py
import argparse
from gendiff.generate import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    path_to_first_file = args.first_file
    path_to_second_file = args.second_file
    diff = generate_diff(path_to_first_file, path_to_second_file)
    print(diff)


if __name__ == '__main__':
    main()
