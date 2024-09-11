# Generate diffrence of data
def build_tree(data1, data2):
    keys = data1.keys() | data2.keys()
    data = {}
    for key in keys:
        if key not in data1:
            data[key] = {'type': 'added', 'key': key, 'value': build_tree(
                data2[key], data2[key]) if isinstance(
                    data2[key], dict) else data2[key]}
        elif key not in data2:
            data[key] = {'type': 'deleted', 'key': key, 'value': build_tree(
                data1[key], data1[key]) if isinstance(
                    data1[key], dict) else data1[key]}
        # elif data1[key] == data2[key]:
        #     data[key] = {'type': 'unchanged', 'key': key, 'value': build_tree(
        #         data1[key], data2[key]) if isinstance(
        #             data1[key], dict) else data1[key]}
        elif isinstance(data1[key], dict):
            data[key] = {'type': 'nested', 'key': key, 'value': build_tree(
                data1[key], data1[key])}
        elif isinstance(data2[key], dict):
            data[key] = {'type': 'nested', 'key': key, 'value': build_tree(
                data2[key], data2[key])}
        # elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
        #     data[key] = {'type': 'nested', 'key': key, 'value': build_tree(
        #         data1[key], data2[key])}
        elif data1[key] != data2[key]:
            data[key] = {
                'type': 'changed', 'key': key, 'value1': data1[key], 'value2': data2[key]
            }
        # elif data1[key] != data2[key]:
        #     data[key] = {'type': 'changed', 'key': key, 'value1': build_tree(
        #         data1[key], data1[key]) if isinstance(
        #             data1[key], dict) else data1[key], 'value2': build_tree(
        #                 data2[key], data2[key]) if isinstance(
        #                     data2[key], dict) else data2[key]}
        # elif isinstance(data1[key], dict) or isinstance(data2[key], dict):
        #     data[key] = {'type': 'nested', 'key': key, 'value': build_tree(
        #         data1[key], data1[key]) if isinstance(
        #             data1[key], dict) else build_tree(
        #                 data2[key], data2[key])}
        # else:
        #    data[key] = {'type': 'children', 'key': key, 'value': data1[key]}
    return data
