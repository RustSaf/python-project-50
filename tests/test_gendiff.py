from gendiff import generate_diff


def test_generate_diff():
    file_diff = open("tests/fixtures/file_result_json.txt")
    diff = file_diff.read()
    file_diff.close()
    assert generate_diff(
            'tests/fixtures/file1.json', 'tests/fixtures/file2.json'
        ) == diff
