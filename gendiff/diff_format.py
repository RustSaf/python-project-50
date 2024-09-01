# Generate format diffrence of json or yaml data
from gendiff.parser import file_parser
from gendiff.generator import generate
import gendiff.format


def generate_diff(file_1, file_2, data_format='stylish'):
    data1 = file_parser(file_1)
    data2 = file_parser(file_2)
    diff = generate(data1, data2)
    formater = getattr(gendiff.format, data_format)
    return formater(diff)
