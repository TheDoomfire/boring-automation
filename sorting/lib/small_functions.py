import re
import os
#import mediainfo


def split_by_first_re_pattern(input_string, patterns): # By first occuring re pattern.
    for pattern in patterns:
        match = re.search(pattern, input_string)
        if match:
            return re.split(pattern, input_string, maxsplit=1)
    # If no pattern is found, return the original string
    return [input_string]


def get_file_extension(file_name):
    empty_variable, file_extension = os.path.splitext(file_name)
    return file_extension, empty_variable


def get_file_path(file_path):
    return os.path.dirname(file_path)


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def delete_empty_folders(path):
    for root, _, files in os.walk(path):
        if not files:
            os.rmdir(root)


""" def file_has_subtitles(filename):
    media_info = mediainfo.MediaInfo()
    media_info.open(filename)
    tracks = media_info.get_tracks()

    for track in tracks:
        if track.track_type == 'Text':
            return True

    return False """