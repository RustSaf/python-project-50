# Formater "Stylish" diffrence of json or yaml data
import json


def make_json(data):
    with open('tests/fixtures/file_result_tmp.json', 'w') as f:
        # json.dump(data, f, sort_keys=True, indent=2)
        json.dump(data, f, sort_keys=True)

    with open('tests/fixtures/file_result_tmp.json') as f:
        result = f.read()

    return result
