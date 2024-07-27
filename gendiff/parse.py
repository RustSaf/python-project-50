#!/usr/bin/env python3
# parser of data in files
import json
import yaml
import sys


def data_parse(file_path1, file_path2):
    if file_path1.endswith('.json') and file_path2.endswith('.json'):
        data1 = json.load(open(file_path1))
        data2 = json.load(open(file_path2))
    elif file_path1.endswith(
            ('.yml', '.yaml')) and file_path2.endswith(
            ('.yml', '.yaml')):
        data1 = yaml.safe_load(open(file_path1))
        data2 = yaml.safe_load(open(file_path2))
    else:
        print("\033[3m\033[31m\033[40m{}\033[0m".format("Unknown file format"))
        sys.exit()

    return data1, data2
