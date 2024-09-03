# Generate diffrence of data
def build_tree(data1, data2):
    keys = data1.keys() | data2.keys()
    data = {}
    for key in keys:
        if key not in data1:
            data[key] = {'key': 'added', 'value': data2[key]}
        elif key not in data2:
            data[key] = {'key': 'deleted', 'value': data1[key]}
        elif data1[key] == data2[key]:
            data[key] = {'key': 'unchanged', 'value': data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            data[key] = build_tree(data1[key], data2[key])
        else:
            data[key] = {
                'key': 'changed', 'value1': data1[key], 'value2': data2[key]
            }
    return data
