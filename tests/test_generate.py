import json
from gendiff import generate_diff
from gendiff.parse import data_parse
from gendiff.generate import generate
from gendiff.format import plain
from gendiff.format import json


def test_diff_json_to_stylish():
    file_diff = open('tests/fixtures/file_result_stylish.txt')
    diff = file_diff.read()
    file_diff.close()
    assert generate_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file2.json'
        ) + '\n' == diff


def test_diff_json_to_plain():
    file_diff = open('tests/fixtures/file_result_plain.txt')
    diff = file_diff.read()
    file_diff.close()
    data1, data2 = data_parse('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    data_diff = generate(data1, data2)
    format_data_diff = plain(data_diff, ["'"], 0)
    assert format_data_diff == diff
    assert generate_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file1.json',
        plain) == ""


def test_diff_yaml_to_stylish():
    file_diff = open('tests/fixtures/file_result_stylish.txt')
    diff = file_diff.read()
    file_diff.close()
    assert generate_diff(
        'tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml'
        ) + '\n' == diff


def test_diff_yaml_to_plain():
    file_diff = open('tests/fixtures/file_result_plain.txt')
    diff = file_diff.read()
    file_diff.close()
    data1, data2 = data_parse('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml')
    data_diff = generate(data1, data2)
    format_data_diff = plain(data_diff, ["'"], 0)
    assert format_data_diff == diff
    assert generate_diff(
        'tests/fixtures/file2.yml', 'tests/fixtures/file2.yml',
        plain) == ""


def test_diff_json_to_json():
    with open('tests/fixtures/file_result.json') as file_diff:
        diff = file_diff.read()
    assert generate_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file2.json',
        json) == diff