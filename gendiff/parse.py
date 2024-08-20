# Parser data of json or yaml files
import json
import yaml
import sys


def data_parse(file_path1, file_path2):
    if file_path1.endswith('.json') and file_path2.endswith('.json'):
        with open(file_path1) as file1:
            data1 = json.load(file1)
        with open(file_path2) as file2:
            data2 = json.load(file2)
    elif file_path1.endswith(
            ('.yml', '.yaml')) and file_path2.endswith(
            ('.yml', '.yaml')):
        with open(file_path1) as file1:
            data1 = yaml.safe_load(file1)
        with open(file_path2) as file2:
            data2 = yaml.safe_load(file2)
    else:
        print("\033[3m\033[31m\033[40m{}\033[0m".format("Unknown file format"))
        sys.exit()

    return data1, data2
