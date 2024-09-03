# Formater "Plain" diffrence of json or yaml data
from gendiff.format.data_to_str import data_to_str


def to_str(data):
    return '[complex value]' if isinstance(
        data, dict) else data_to_str(data, 1)


def make_plain(data, path="'", i=0):
    keys = sorted(data.keys())
    result = ""
    beginpath = []
    for key in keys:
        if data[key].get('key') == 'added':
            result += (
                f"Property {path}{key}' was added with value: "
                f"{to_str(data[key].get('value'))}\n"
            )
            i += 1
        elif data[key].get('key') == 'deleted':
            result += f"Property {path}{key}' was removed\n"
            i += 1
        elif data[key].get('key') == 'changed':
            result += (
                f"Property {path}{key}' was updated. From "
                f"{to_str(data[key].get('value1'))} to "
                f"{to_str(data[key].get('value2'))}\n"
            )
            i += 2
        elif data[key].get('key') == 'unchanged':
            i += 1
        else:
            beginpath.append(path)
            path = f"{path}{key}."
            i += 1
            result += make_plain(data[key], path, i)
            path = beginpath[0]
    return result if i != len(keys) else result.rstrip('\n')
