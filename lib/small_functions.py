import re


def split_by_first_re_pattern(input_string, patterns):
    for pattern in patterns:
        match = re.search(pattern, input_string)
        if match:
            return re.split(pattern, input_string, maxsplit=1)
    # If no pattern is found, return the original string
    return [input_string]
