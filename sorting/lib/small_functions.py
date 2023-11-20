import re
import os


def split_by_first_re_pattern(input_string, patterns): # By first occuring re pattern.
    for pattern in patterns:
        match = re.search(pattern, input_string)
        if match:
            return re.split(pattern, input_string, maxsplit=1)
    # If no pattern is found, return the original string
    return [input_string]


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def get_file_extension(file_name):
    emptyVar, file_extension = os.path.splitext(file_name)
    return file_extension
