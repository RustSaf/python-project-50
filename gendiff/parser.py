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
    match ext_file:
        case '.json':
            data = json.load(file)
            return data
        case '.yaml':
            data = yaml.safe_load(file)
            return data
        case '.yml':
            data = yaml.safe_load(file)
            return data
        case _:
            raise ValueError("\033[3m\033[31m\033[40m{}\033[0m".format(
                "Unknown file format"))
