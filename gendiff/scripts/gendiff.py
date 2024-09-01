#!/usr/bin/env python3
# script: gendiff.py
from gendiff.arg_parser import arg_parser
from gendiff.diff_format import generate_diff


def main():
    file1, file2, format = arg_parser()
    diff = generate_diff(file1, file2, format)
    print(diff)


if __name__ == '__main__':
    main()
