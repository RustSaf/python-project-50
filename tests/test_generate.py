from gendiff import generate_diff


def test_generate_diff_json():
    file_diff = open("tests/fixtures/file_result.txt")
    diff = file_diff.read()
    file_diff.close()
    assert generate_diff(
            'tests/fixtures/file1.json', 'tests/fixtures/file2.json'
        ) == diff


def test_generate_diff_yaml():
    file_diff = open("tests/fixtures/file_result.txt")
    diff = file_diff.read()
    file_diff.close()
    assert generate_diff(
            'tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml'
        ) == diff
