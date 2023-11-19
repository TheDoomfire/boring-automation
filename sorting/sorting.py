import os
import re

# Custom Imports
import variables # On main app gets the error "no module named 'variables'"


def split_by_first_re_pattern(input_string, patterns):
    for pattern in patterns:
        match = re.search(pattern, input_string)
        if match:
            return re.split(pattern, input_string, maxsplit=1)
    # If no pattern is found, return the original string
    return [input_string]


def contains_regex(text, pattern):
    match = re.search(pattern, text)
    return match is not None


# TODO: Create a function called "format_name"
# that returns a formatted name and file/folder name?
# and movie name or serie name.

def format_file_name(file_name):
    # variables.RE_SERIE, variables.RE_YEAR, variables.RE_VIDEO_PIXELS
    pattern_serie = re.compile(variables.RE_SERIE)
    pattern_year = re.compile(variables.RE_YEAR)
    pattern_pixel = re.compile(variables.RE_VIDEO_PIXELS)

    match_serie = pattern_serie.search(file_name)
    match_year = pattern_year.search(file_name)
    match_pixel = pattern_pixel.search(file_name)

    print("YEAR: ", match_year)
    print("SERIE: ", match_serie)
    print("PIXEL: ", match_pixel)


def sorter(folder_path):
    video_files = []
    try:
    # Check if the folder path exists
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")
        
        # Iterate through files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # Check if the file is a regular file and has a video extension
            if os.path.isfile(file_path) and any(file_path.lower().endswith(ext) for ext in variables.EXTENSION_VIDEOS):
                video_files.append(file_path)
                print(filename)
                format_file_name(filename)
                print("Name: ", split_by_first_re_pattern(filename, [variables.RE_SERIE, variables.RE_YEAR, variables.RE_VIDEO_PIXELS])[0])
                print("Video: ", contains_regex(filename, variables.RE_YEAR))
                print("Serie: ", contains_regex(filename, variables.RE_SERIE)) # checks for 'S01E02' format
                # TODO: Check if movie, serie or else? Preferable by re first then format name

        #print(video_files)

    except Exception as e:
        return str(e)


def main():
    sorter(r"D:\Downloads\2 - Torrents")
"""     if isinstance(movies, list):
        print("Movie files found:")
        for movie in movies:
            print(movie)
    else:
        print("Error:", movies) """


if __name__ == '__main__':
    main()