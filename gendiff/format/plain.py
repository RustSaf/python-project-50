# Formater "Plain" diffrence of json or yaml data
from gendiff.format.data_to_str import data_to_str


def make_plain(data, paths=["'"], i=0):
    keys = sorted(data.keys())
    result = ""
    n = 0
    endpath = ''
    for k, key in enumerate(keys):
        if isinstance(data[key], dict):
            if 'added' in data[key]:
                result += 'Property ' + paths[i-n] + f"{key}'" + (
                    ' was added with value: ' + (
                        '[complex value]' if isinstance(
                            data[key].get('added'), dict) else data_to_str(
                                data[key].get('added'), 1)) + '\n'
                )
            elif 'deleted' in data[key]:
                result += 'Property ' + paths[i-n] + f"{key}'" + (
                    ' was removed' + '\n'
                )
            elif 'old' and 'new' in data[key]:
                result += 'Property ' + paths[i-n] + f"{key}'" + (
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
            elif 'unchanged' in data[key]:
                continue
            else:
                path = paths[i] + f"{key}."
                paths.append(path)
                i += 1
                n += 1
                result += make_plain(data[key], paths, i)
                endpath = paths[i]
            paths = list(
                map(lambda x: paths[i-1] if x == endpath else x, paths))
    return result if n == 0 else (
               result.rstrip('\n') if paths[-1] == "'" else result)
