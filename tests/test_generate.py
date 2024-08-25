import json
from gendiff import generate_diff
from gendiff.parse import data_parse
from gendiff.generate import generate
from gendiff.format import stylish
from gendiff.format import plain
from gendiff.format import json


def test_diff_json_to_stylish():
    with open('tests/fixtures/file_result_stylish.txt') as file_diff:
        diff = file_diff.read()
    assert generate_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file2.json',
        'stylish') + '\n' == diff


def test_diff_json_to_plain():
    with open('tests/fixtures/file_result_plain.txt') as file_diff:
        diff = file_diff.read()
    data1, data2, format = data_parse('tests/fixtures/file1.json',
        'tests/fixtures/file2.json', 'plain')
    data_diff = generate(data1, data2)
    format_data_diff = format(data_diff, ["'"], 0)
    assert format_data_diff + '\n' == diff
    assert generate_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file1.json',
        'plain') == ""


def test_diff_yaml_to_stylish():
    with open('tests/fixtures/file_result_stylish.txt') as file_diff:
        diff = file_diff.read()
    assert generate_diff(
        'tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml',
        'stylish') + '\n' == diff


def test_diff_yaml_to_plain():
    with open('tests/fixtures/file_result_plain.txt') as file_diff:
        diff = file_diff.read()
    data1, data2, format = data_parse('tests/fixtures/file1.yaml',
        'tests/fixtures/file2.yml', 'plain')
    data_diff = generate(data1, data2)
    format_data_diff = format(data_diff, ["'"], 0)
    assert format_data_diff + '\n' == diff
    assert generate_diff(
        'tests/fixtures/file2.yml', 'tests/fixtures/file2.yml',
        'plain') == ""


def test_diff_json_to_json():
    with open('tests/fixtures/file_result.json') as file_diff:
        diff = file_diff.read()
    assert generate_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file2.json',
        'json') == diff
