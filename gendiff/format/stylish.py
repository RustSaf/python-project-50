# Formater "Stylish" diffrence of json or yaml data
from gendiff.format.data_to_str import data_to_str


def make_stylish(data, i=0):
    keys = sorted(data.keys())
    result = ""
    for key in keys:
        if isinstance(data[key], dict):
            if 'added' in data[key]:
                result += '    '*i + '  + ' + key + ': ' + data_to_str(
                    make_stylish(data[key].get('added'), i+1) if isinstance(
                        data[key].get('added'), dict
                    ) else data[key].get('added')) + '\n'
            elif 'deleted' in data[key]:
                result += '    '*i + '  - ' + key + ': ' + data_to_str(
                    make_stylish(data[key].get('deleted'), i+1) if isinstance(
                        data[key].get('deleted'), dict
                    ) else data[key].get('deleted')) + '\n'
            elif 'unchanged' in data[key]:
                result += '    '*i + '    ' + key + ': ' + data_to_str(
                    make_stylish(data[key].get(
                        'unchanged'), i+1) if isinstance(
                            data[key].get('unchanged'), dict
                                ) else data[key].get('unchanged')) + '\n'
            elif 'old' and 'new' in data[key]:
                result += '    '*i + '  - ' + key + ': ' + data_to_str(
                    make_stylish(data[key].get('old'), i+1) if isinstance(
                        data[key].get('old'), dict
                    ) else data[key].get('old')) + '\n'
                result += '    '*i + '  + ' + key + ': ' + data_to_str(
                    make_stylish(data[key].get('new'), i+1) if isinstance(
                        data[key].get('new'), dict
                    ) else data[key].get('new')) + '\n'
            else:
                result += '    '*(i+1) + key + ': ' + data_to_str(
                    make_stylish(data[key], i+1)) + '\n'
        else:
            result += '    '*(i+1) + key + ': ' + data_to_str(data[key]) + '\n'
    return '{\n' + result + '    '*i + '}'
