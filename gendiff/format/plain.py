# Formater "Plain" diffrence of json or yaml data
from gendiff.format.data_to_str import data_to_str


def make_plain(data, path="'", i=0):
    keys = sorted(data.keys())
    result = ""
    beginpath = []
    for k, key in enumerate(keys):
        if isinstance(data[key], dict):
            if 'added' in data[key]:
                result += 'Property ' + path + f"{key}'" + (
                    ' was added with value: ' + (
                        '[complex value]' if isinstance(
                            data[key].get('added'), dict) else data_to_str(
                                data[key].get('added'), 1)) + '\n'
                )
                i += 1
            elif 'deleted' in data[key]:
                result += 'Property ' + path + f"{key}'" + (
                    ' was removed' + '\n'
                )
                i += 1
            elif 'old' and 'new' in data[key]:
                result += 'Property ' + path + f"{key}'" + (
                    ' was updated. From ' + (
                        '[complex value]' if isinstance(
                            data[key].get('old'), dict) else data_to_str(
                                data[key].get('old'), 1)) + ' to ' + (
                                    '[complex value]' if isinstance(
                                        data[key].get('new'), dict) else (
                                            data_to_str(
                                                data[key].get('new'), 1))
                    ) + '\n'
                )
                i += 2
            elif 'unchanged' in data[key]:
                i += 1
            else:
                beginpath.append(path)
                path = path + f"{key}."
                i += 1
                result += make_plain(data[key], path, i)
                path = beginpath[0]
    return result if i != len(keys) else result.rstrip('\n')
