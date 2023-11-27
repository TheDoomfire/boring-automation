import re
import os
import requests
import zipfile
#import mediainfo

import variables


def split_by_first_re_pattern(input_string, patterns): # By first occuring re pattern.
    for pattern in patterns:
        match = re.search(pattern, input_string)
        if match:
            return re.split(pattern, input_string, maxsplit=1)
    # If no pattern is found, return the original string
    return [input_string]


def get_file_extension(file_name):
    file_name_without_extension, file_extension = os.path.splitext(file_name)
    return file_extension, file_name_without_extension


def get_file_path(file_path):
    return os.path.dirname(file_path)


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def delete_empty_folders(path):
    for root, _, files in os.walk(path):
        if not files:
            os.rmdir(root)


def split_by_this(split_this, splitter):
    return list(filter(None, split_this.split(splitter)))


def split_by_this_and_remove_single_chars(split_this, splitter):
    return [item for item in split_this.split(splitter) if len(item) > 1]


def split_by_these_and_remove_single_chars(text, delimiters):
    for delimiter in delimiters:
        if delimiter == "":
            text = " ".join(text.split())
        else:
            text = " ".join(text.split(delimiter))

    result = text.split()
    return result


def remove_short_strings(input_list, short_string=1):
    # Use list comprehension to filter out elements with length <= 1
    result_list = [item for item in input_list if len(str(item)) > short_string]
    return result_list


def count_common_elements(list1, list2):
    # Convert lists to sets, with elements converted to lowercase
    set1 = set(map(str.lower, list1))
    set2 = set(map(str.lower, list2))

    # Find the intersection of the sets (common elements)
    common_elements = set1.intersection(set2)

    # Return the count of common elements
    return len(common_elements)



def remove_special_characters(input_string):
    special_characters = variables.LIST_ALL_SPECIAL_CHARACTERS
    cleaned_string = ''.join(char for char in input_string if char not in special_characters)
    return cleaned_string


def download_file(url, save_dir):
    # Create the save directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Download the file
    response = requests.get(url)

    # Check if the download was successful
    if response.status_code == 200:
        # Get the filename from the Content-Disposition header
        content_disposition = response.headers.get('Content-Disposition')
        if content_disposition:
            filename = content_disposition.split(';')[1].strip().split('=')[1].strip("'\"")
        else:
            filename = os.path.basename(url)

        # Save the file to the specified directory
        with open(os.path.join(save_dir, filename), 'wb') as f:
            f.write(response.content)

        print("File downloaded successfully")
        return os.path.join(save_dir, filename)
    else:
        print("Error downloading file:", response.status_code)
        return None



def unzip_file(zip_file_path, extract_to):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    # TODO: Might need a safeguard, so it only removes IF it successfully extracted all.
    os.remove(zip_file_path)


def find_archive_files(directory):
    # List all files in the directory
    all_files = os.listdir(directory)

    # Filter files based on the specified extensions
    archive_files = [file for file in all_files if any(file.endswith(ext) for ext in variables.EXTENSION_ARCHIVES)]

    return archive_files


def find_subtitle_files(directory):
    # List all files in the directory
    all_files = os.listdir(directory)

    # Filter files based on the specified extensions
    subtitle_files = [file for file in all_files if any(file.endswith(ext) for ext in variables.EXTENSION_SUBTITLES)]

    return subtitle_files


def list_folders(directory):
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    return folders



""" def file_has_subtitles(filename):
    media_info = mediainfo.MediaInfo()
    media_info.open(filename)
    tracks = media_info.get_tracks()

    for track in tracks:
        if track.track_type == 'Text':
            return True

    return False """