# Formater "Plain" diffrence of json or yaml data
from gendiff.format.data_to_str import data_to_str


def format_value(data):
    return '[complex value]' if isinstance(
        data, dict) else data_to_str(data, 1)


def make_plain(data, path="'", i=0):
    keys = sorted(data.keys())
    result = ""
    beginpath = []
    for key in keys:
        if 'added' in data[key]:
            result += (
                f"Property {path}{key}' was added with value: "
                f"{format_value(data[key].get('added'))}\n"
            )
            i += 1
        elif 'deleted' in data[key]:
            result += f"Property {path}{key}' was removed\n"
            i += 1
        elif 'old' and 'new' in data[key]:
            result += (
                f"Property {path}{key}' was updated. From "
                f"{format_value(data[key].get('old'))} to "
                f"{format_value(data[key].get('new'))}\n"
            )
            i += 2
        elif 'unchanged' in data[key]:
            i += 1
        else:
            beginpath.append(path)
            path = f"{path}{key}."
            i += 1
            result += make_plain(data[key], path, i)
            path = beginpath[0]
    return result if i != len(keys) else result.rstrip('\n')
