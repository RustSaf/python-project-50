### Hexlet tests and linter status:

[![GitHub Actions Status](https://github.com/RustSaf/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/RustSaf/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/2970babfb69a24ebb786/maintainability)](https://codeclimate.com/github/RustSaf/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2970babfb69a24ebb786/test_coverage)](https://codeclimate.com/github/RustSaf/python-project-50/test_coverage)

### Overview and Installation

A difference calculator is a program that determines the difference between two data structures. This is a popular task, 
for which there are many online services, such as jsondiff. A similar mechanism is, for example, used when outputting 
tests or automatically tracking changes in configuration files.

Utility features:

   * Supports different input formats: yaml, json
   * Generating a report in the form of plain text, stylish and json



_Install the pip package using the command:_

```python

$ python3 -m pip install --user dist/*.whl

```


Our program compares two configuration files. This means that the cli utility can accept two arguments via the command line - 
paths to these files. The result of file comparison can be output in different formats, for example: plain ("flat") or json 
("JSON format"). Help information for our utility looks like this:

```python

$gendiff -h
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output

```

The differential is built based on how the contents in the second file have changed relative to the first. Keys are displayed in 
alphabetical order. Below is an example of what should be the result of this step:

```python

$gendiff filepath1.json filepath2.json
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}

```


The absence of a plus or minus indicates that the key is in both files and its values ​​are the same. In all other situations, 
the value of the key is either different, or the key is in only one file. In the example above, the _timeout_ key is in both files, 
but has different meanings. _Proxy_ is only in _file1.json_ and _verbose_ is only in _file2.json_.


You can install this package as a dependency and add it to yourself for use in your code. 
Example:

```python

from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2)
print(diff)

```


### Usage

Examples of usage "gendiff" on ![asciinema.org](https://asciinema.org).


_Launching the gendiff and finding differences in json files:_

[![asciicast2](https://asciinema.org/a/qbOmbJ1bQ4UyNXGwZPaC18w1P.png)](https://asciinema.org/a/qbOmbJ1bQ4UyNXGwZPaC18w1P)

_Launching the gendiff and finding differences in json and yaml files:_

[![asciicast2](https://asciinema.org/a/rVkwHmakVdDJLWv8dI9M5ji3V.png)](https://asciinema.org/a/rVkwHmakVdDJLWv8dI9M5ji3V)


### Links

_This project was built using these tools_:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://python-poetry.org/)                                        | "Python dependency management and packaging made easy"  |
| [Py.Test](https://pytest.org/)                                              | "A mature full-featured Python testing tool"            |
| [flake8](https://flake8.pycqa.org/)                                         | "Your tool for style guide enforcement"                 |

---
