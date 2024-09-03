# Formater "Stylish" diffrence of json or yaml data
from gendiff.format.data_to_str import data_to_str


def make_stylish(data, i=0):
    keys = sorted(data.keys())
    result = ""
    INDENT = '    '
    for key in keys:
        if isinstance(data[key], dict):
            if data[key].get('key') == 'added':
                result += (
                    f"{INDENT * i}  + {key}: "
                    f"""{data_to_str(make_stylish(data[key].get('value'),
                         i + 1) if isinstance(data[key].get('value'), dict)
                         else data[key].get('value'))}\n"""
                )
            elif data[key].get('key') == 'deleted':
                result += (
                    f"{INDENT * i}  - {key}: "
                    f"""{data_to_str(make_stylish(data[key].get('value'),
                         i + 1) if isinstance(data[key].get('value'), dict)
                         else data[key].get('value'))}\n"""
                )
            elif data[key].get('key') == 'unchanged':
                result += (
                    f"{INDENT * i}    {key}: "
                    f"""{data_to_str(make_stylish(data[key].get('value'),
                         i + 1) if isinstance(data[key].get('value'), dict)
                         else data[key].get('value'))}\n"""
                )
            elif data[key].get('key') == 'changed':
                result += (
                    f"{INDENT * i}  - {key}: "
                    f"""{data_to_str(make_stylish(data[key].get('value1'),
                         i + 1) if isinstance(data[key].get('value1'), dict)
                         else data[key].get('value1'))}\n"""
                )
                result += (
                    f"{INDENT * i}  + {key}: "
                    f"""{data_to_str(make_stylish(data[key].get('value2'),
                         i + 1) if isinstance(data[key].get('value2'), dict)
                         else data[key].get('value2'))}\n"""
                )
            else:
                result += (
                    f"{INDENT * (i + 1)}{key}: "
                    f"{data_to_str(make_stylish(data[key], i + 1))}\n"
                )
        else:
            result += f"{INDENT * (i + 1)}{key}: {data_to_str(data[key])}\n"
    return f"{{\n{result}{INDENT * i}}}"
