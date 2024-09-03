# Generate format diffrence of json or yaml data
from gendiff.parser import file_parser
from gendiff.generator import build_tree
import gendiff.format


def formater(data_form):
    return getattr(gendiff.format, data_form)


def generate_diff(file_1, file_2, data_format='stylish'):
    try:
        data1 = file_parser(file_1)
        data2 = file_parser(file_2)
        diff = build_tree(data1, data2)
    except AttributeError:
        return "\033[3m\033[31m\033[40m{}\033[0m".format("Unknown file format")
    return formater(data_format)(diff)
