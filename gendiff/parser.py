# Parser data of json or yaml files
import json
import yaml
from pathlib import Path


def file_parser(filename):
    with open(filename) as file:
        ext = Path(filename).suffix
        data = data_parser(file, ext)
    return data


def data_parser(file, ext_file):
    if ext_file == '.json':
        data = json.load(file)
    elif ext_file == '.yaml' or '.yml':
        data = yaml.safe_load(file)
    return data
