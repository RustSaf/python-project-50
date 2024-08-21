#!/usr/bin/env python3
# Generate diffrence of json or yaml data
from gendiff.parse import data_parse
from gendiff.format import stylish
from gendiff.format import plain # noqa


def generate(data1, data2):
    keys = data1.keys() | data2.keys()
    data = {}
    for key in keys:
        if key not in data1:
            data[key] = {'added': data2[key]}
        elif key not in data2:
            data[key] = {'deleted': data1[key]}
        elif data1[key] == data2[key]:
            data[key] = {'unchanged': data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            data[key] = generate(data1[key], data2[key])
        else:
            data[key] = {'old': data1[key], 'new': data2[key]}
    return data


def generate_diff(file_1, file_2, data_format='stylish'):
    data1, data2 = data_parse(file_1, file_2)
    diff = generate(data1, data2)
    format_diff = data_format(diff)
    return format_diff
