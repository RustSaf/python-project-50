# Generate format diffrence of json or yaml data
from gendiff.parser import file_parser
from gendiff.generator import build_tree
from gendiff.format import formater


def generate_diff(file_1, file_2, data_format='stylish'):
    data1 = file_parser(file_1)
    data2 = file_parser(file_2)
    diff = build_tree(data1, data2)
    return formater(data_format)(diff)
