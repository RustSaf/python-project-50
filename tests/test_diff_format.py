from gendiff.diff_format import generate_diff
from gendiff.parser import file_parser
from gendiff.generator import build_tree
from gendiff.format import formater


def test_diff_json_to_stylish():
    with open('tests/fixtures/file_result_stylish.txt') as file_diff:
        diff_test = file_diff.read()
    assert generate_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file2.json',
        'stylish') + '\n' == diff_test


def test_diff_json_to_plain():
    with open('tests/fixtures/file_result_plain.txt') as file_diff:
        diff_test = file_diff.read()
    data1 = file_parser('tests/fixtures/file1.json')
    data2 = file_parser('tests/fixtures/file2.json')
    diff = build_tree(data1, data2)
    format_diff = formater('plain')(diff)
    assert format_diff + '\n' == diff_test
    assert generate_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file1.json',
        'plain') == "\n\n"


def test_diff_yaml_to_stylish():
    with open('tests/fixtures/file_result_stylish.txt') as file_diff:
        diff_test = file_diff.read()
    assert generate_diff(
        'tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml',
        'stylish') + '\n' == diff_test


def test_diff_yaml_to_plain():
    with open('tests/fixtures/file_result_plain.txt') as file_diff:
        diff_test = file_diff.read()
    data1 = file_parser('tests/fixtures/file1.yaml')
    data2 = file_parser('tests/fixtures/file2.yml')
    diff = build_tree(data1, data2)
    format_diff = formater('plain')(diff)
    assert format_diff + '\n' == diff_test
    assert generate_diff(
        'tests/fixtures/file1.yaml', 'tests/fixtures/file1.yaml',
        'plain') == "\n\n"


def test_diff_json_or_yaml_to_json():
    with open('tests/fixtures/file_result.json') as file_diff:
        diff_test = file_diff.read()
    assert generate_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file2.json',
        'json') == diff_test
    assert generate_diff(
        'tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml',
        'json') == diff_test
