from gendiff import generate_diff
#from gendiff import stylish


def main():
    generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', stylish)


if __name__ == '__main__':
    main()
