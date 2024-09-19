# Formater "Stylish" diffrence of json or yaml data
from gendiff.format.data_to_str import data_to_str


INDENT = '    '


def to_str(data, depth=0):
    result_lines = ''
    if isinstance(data, dict):
        keys = sorted(data.keys())
        result = []
        formatted_lines = []
        for key in keys:
            formatted_lines = data_to_str(to_str(data[key].get('value'), depth + 1))
            sub_result = '\n'.join(formatted_lines)
            result.append(f"{INDENT*depth}  {key}: {sub_result}\n")
        result_lines = '\n'.join(result)
    #else:
    #    formatted_value = data_to_str(data[])
    #    sub_result.append(f"{formatted_value}\n")
    return result_lines


def make_stylish(data, depth=0):
    result_lines = ''
    keys = sorted(data.keys())
    result = []
    lines = []
    for key in keys:
        if data[key].get('type') == 'added':
            result.append(f"{INDENT*depth}+ {key}: "
                          f"{to_str(data[key].get('value'), depth)}\n")
        elif data[key].get('type') == 'deleted':
            result.append(f"{INDENT*depth}- {key}: "
                          f"{to_str(data[key].get('value'), depth)}\n")
        elif data[key].get('type') == 'changed':
            result.append(f"{INDENT*depth}- {key}: "
                          f"{to_str(data[key].get('value1'), depth)}\n")
            result.append(f"{INDENT*depth}+ {key}: "
                          f"{to_str(data[key].get('value2'), depth)}\n")
        elif data[key].get('type') == 'children':
            result.append(f"{INDENT*depth}  {key}: "
                          f"{to_str(data[key].get('value'), depth)}\n")
        elif data[key].get('type') == 'nested':
            #lines = list(map(lambda child: make_stylish(
            #    child, depth + 1), data[key].get('value')))
            lines = make_stylish(data[key].get('value'), depth + 1)
            sub_result = '\n'.join(lines)
            result.append(f"{INDENT*depth}  {key}: {sub_result}\n")
    result_lines = '\n'.join(result)
    return result_lines
