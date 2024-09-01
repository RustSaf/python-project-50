# Parser data of json or yaml files
import json
import yaml
import sys


def file_parser(file_path):
    if file_path.endswith('.json'):
        with open(file_path) as file:
            data = data_parser(file, 'json')
    elif file_path.endswith(('.yml', '.yaml')):
        with open(file_path) as file:
            data = data_parser(file, 'yaml')
    else:
        print("\033[3m\033[31m\033[40m{}\033[0m".format("Unknown file format"))
        sys.exit()
    return data


def data_parser(data_file, format_file):
    if format_file == 'json':
        data = json.load(data_file)
    elif format_file == 'yaml':
        data = yaml.safe_load(data_file)
    return data
