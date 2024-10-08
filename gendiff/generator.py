# Generate diffrence of data
def build_tree(data1, data2):
    keys = data1.keys() | data2.keys()
    data = {}
    for key in keys:
        if key not in data1:
            data[key] = {'type': 'added', 'value': build_tree(
                data2[key], data2[key]) if isinstance(
                    data2[key], dict) else data2[key]}
        elif key not in data2:
            data[key] = {'type': 'deleted', 'value': build_tree(
                data1[key], data1[key]) if isinstance(
                    data1[key], dict) else data1[key]}
        elif data1[key] == data2[key]:
            if isinstance(data1[key], dict):
                data[key] = {'type': 'nested', 'value': build_tree(
                    data1[key], data1[key])}
            else:
                data[key] = {
                    'type': 'children', 'value': data1[key]}
        elif data1[key] != data2[key]:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                data[key] = {'type': 'nested', 'value': build_tree(
                    data1[key], data2[key])}
            else:
                data[key] = {
                    'type': 'changed', 'value1': build_tree(
                        data1[key], data1[key]) if isinstance(
                            data1[key], dict) else data1[
                                key], 'value2': build_tree(
                                    data2[key], data2[key]) if isinstance(
                                        data2[key], dict) else data2[key]}
    return data
