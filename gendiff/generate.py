#!/usr/bin/env python3
# engine of games
import json


def generate_diff(file_path1, file_path2):
    d1 = json.load(open(file_path1))
    d2 = json.load(open(file_path2))
    keys = sorted(d1.keys() | d2.keys())
    result = ''

    def data_to_str(d, key):
        return str(d[key]).lower() if isinstance(d[key], bool) else str(d[key])

    for key in keys:
        if key not in d1:
            result = result + '+ ' + key + ': ' + data_to_str(d2, key) + '\n'
        elif key not in d2:
            result = result + '- ' + key + ': ' + data_to_str(d1, key) + '\n'
        elif d1[key] == d2[key]:
            result = result + '  ' + key + ': ' + data_to_str(d1, key) + '\n'
        else:
            result = result + '- ' + key + ': ' + data_to_str(d1, key) + '\n'
            result = result + '+ ' + key + ': ' + data_to_str(d2, key) + '\n'

    return '{\n' + result + '}'
