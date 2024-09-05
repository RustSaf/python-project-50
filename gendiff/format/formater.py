# Get formatter for diff
import gendiff.format


def get_formater(data_form):
    match data_form:
        case 'stylish':
            return gendiff.format.stylish
        case 'plain':
            return gendiff.format.plain
        case 'json':
            return gendiff.format.json
        case _:
            raise Exception("\033[3m\033[31m\033[40m{}\033[0m".format(
                "Unknown formater"))
