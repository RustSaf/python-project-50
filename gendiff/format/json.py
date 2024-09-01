# Formater "Json" diffrence of json or yaml data
import json


def make_json(data):
    result = json.dumps(data, sort_keys=True, indent=2)
    return result
