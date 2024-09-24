# Formater "Stylish" diffrence of json or yaml data
from gendiff.format.data_to_str import data_to_str


INDENT = '    '


def to_str(data, depth=0):
    result_line = ''
    result = []
    if isinstance(data, dict):
        keys = sorted(data.keys())
        for key in keys:
        #    if data[key].get('type') != 'children':
        #        result.append(f"{INDENT*depth}    {key}: "
        #                      f"{data_to_str(data[key].get('value'))}")
        #    else:
            result.append(f"{{\n{INDENT*(depth + 1)}{key}: "
                          f"{data_to_str(to_str(data[key].get('value'), depth + 1))}"
                          f"\n{INDENT*depth}}}")
            #else:
            #    result.append(f"{INDENT*(depth+1)}  {key}: "
            #                  f"{data_to_str(data[key].get('value'))}")
                              # f"\n{INDENT}  }}")
    else:
        result.append(f"{data_to_str(data)}")
    result_line = '\n'.join(result)
    return f"{result_line}"

def make_stylish(data, depth=0):
    result_line = ''
    result = []
    keys = sorted(data.keys())
    for key in keys:
        if data[key].get('type') == 'added':
            result.append(f"{INDENT*depth}  + {key}: "
                          f"{to_str(data[key].get('value'), depth + 1)}")
        elif data[key].get('type') == 'deleted':
            result.append(f"{INDENT*depth}  - {key}: "
                          f"{to_str(data[key].get('value'), depth + 1)}")
        elif data[key].get('type') == 'changed':
            result.append(f"{INDENT*depth}  - {key}: "
                          f"{to_str(data[key].get('value1'), depth + 1)}")
            result.append(f"{INDENT*depth}  + {key}: "
                          f"{to_str(data[key].get('value2'), depth + 1)}")
        elif data[key].get('type') == 'children':
            result.append(f"{INDENT*depth}    {key}: "
                          f"{data_to_str(data[key].get('value'))}")
        else:
            # lines = list(map(lambda child: make_stylish(
            #     child, depth + 1), data[key].get('value')))
            # lines = map(lambda child: make_stylish(child, depth + 1), data[key].get('value'))
            # sub_result = '\n'.join(lines)
            # result.append(f"{INDENT}  {key}: {{\n{sub_result}\n{INDENT}  }}")
            result.append(
                          f"{INDENT*(depth + 1)}{key}: "
                          f"{make_stylish(data[key].get('value'), depth + 1)}"
                          f"\n{INDENT*(depth + 1)}}}")
    result_line = '\n'.join(result)
    return f"{{\n{result_line}"
