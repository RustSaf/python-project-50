#!/usr/bin/env python3
# engine of games
from gendiff.parse import data_parse


def data_to_str(d, key):
    return str(d[key]).lower() if isinstance(d[key], bool) else str(d[key])


def generate_diff(file1, file2):
    dat1, dat2 = data_parse(file1, file2)
    keys = sorted(dat1.keys() | dat2.keys())
    result = ''
    for key in keys:
        if key not in dat1:
            result = result + '+ ' + key + ': ' + data_to_str(dat2, key) + '\n'
        elif key not in dat2:
            result = result + '- ' + key + ': ' + data_to_str(dat1, key) + '\n'
        elif dat1[key] == dat2[key]:
            result = result + '  ' + key + ': ' + data_to_str(dat1, key) + '\n'
        else:
            result = result + '- ' + key + ': ' + data_to_str(dat1, key) + '\n'
            result = result + '+ ' + key + ': ' + data_to_str(dat2, key) + '\n'

    return '{\n' + result + '}'
