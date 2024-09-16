# Formater "Plain" diffrence of json or yaml data
from gendiff.format.data_to_str import data_to_str


def to_str(data):
    return '[complex value]' if isinstance(
        data, dict) else data_to_str(data, 1)


def make_plain(data, path=""):
    keys = sorted(data.keys())
    result = []
    beginpath = []
    for key in keys:
        if data[key].get('type') == 'added':
            result.append(
                f"Property '{path}{key}' was added with value: "
                f"{to_str(data[key].get('value'))}"
            )
        elif data[key].get('type') == 'deleted':
            result.append(f"Property '{path}{key}' was removed")
        elif data[key].get('type') == 'changed':
            result.append(
                f"Property '{path}{key}' was updated. From "
                f"{to_str(data[key].get('value1'))} to "
                f"{to_str(data[key].get('value2'))}"
            )
        elif data[key].get('type') == 'children':
            pass
        elif data[key].get('type') == 'nested':
            beginpath.append(path)
            path = f"{path}{key}."
            result.append(make_plain(data[key].get('value'), path))
            path = beginpath[0]
        else:
            pass
    return '\n'.join(result)
