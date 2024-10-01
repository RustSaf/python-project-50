# Formater "Stylish" diffrence of json or yaml data
from gendiff.format.data_to_str import data_to_str


INDENT = '    '


def to_str(data, depth=0):
    result_line = ''
    result = []
    if isinstance(data, dict):
        keys = sorted(data.keys())
        for key in keys:
            if data[key].get('type') == 'children':
                result.append(f"{INDENT * (depth + 1)}{key}: "
                              f"{data_to_str(data[key].get('value'))}")
            else:
                result.append(f"{INDENT * (depth + 1)}{key}: "
                              f"{to_str(data[key].get('value'), depth + 1)}")
    else:
        return data_to_str(data)
    result_line = '\n'.join(result)
    return f"{{\n{result_line}\n{INDENT * depth}}}"


def make_stylish(data, depth=0):
    result_line = ''
    result = []
    keys = sorted(data.keys())
    for key in keys:
        if data[key].get('type') == 'added':
            result.append(f"{INDENT * depth}  + {key}: "
                          f"{to_str(data[key].get('value'), depth + 1)}")
        elif data[key].get('type') == 'deleted':
            result.append(f"{INDENT * depth}  - {key}: "
                          f"{to_str(data[key].get('value'), depth + 1)}")
        elif data[key].get('type') == 'changed':
            result.append(f"{INDENT * depth}  - {key}: "
                          f"{to_str(data[key].get('value1'), depth + 1)}")
            result.append(f"{INDENT * depth}  + {key}: "
                          f"{to_str(data[key].get('value2'), depth + 1)}")
        elif data[key].get('type') == 'children':
            result.append(f"{INDENT * depth}    {key}: "
                          f"{to_str(data[key].get('value'))}")
        else:
            result.append(f"{INDENT * (depth + 1)}{key}: "
                          f"{make_stylish(data[key].get('value'), depth + 1)}")
    result_line = '\n'.join(result)
    return f"{{\n{result_line}\n{INDENT * depth}}}"
