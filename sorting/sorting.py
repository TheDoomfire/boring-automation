import os
import re
import shutil

# Custom Imports
import variables # On main app gets the error "no module named 'variables'"
from checking import media
from lib import small_functions


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


# For getting the episode and season. 
def extract_season_episode(filename):
    # Check for 's01e02' format
    match = re.search(variables.RE_SERIE, filename, re.IGNORECASE)
    if match:
        season = match.group(1)
        episode = match.group(2)
        return int(season), int(episode)

    else:
        return None, None


def extract_numbers(text):
    numbers = re.findall(variables.RE_NUMBERS, text)
    return numbers


def clean_text(input_text):
    # Replace non-alphanumeric characters with spaces
    replaced_text = re.sub(r'[^a-zA-Z0-9]', ' ', input_text)
    
    # Remove excess spaces and strip leading and trailing spaces
    cleaned_text = ' '.join(replaced_text.split())

    # Capitalize the first letter of each word and convert the rest to lowercase
    cleaned_text = cleaned_text.title()
    
    return cleaned_text


def two_digits(n):
  return "%02d" % n

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

    season = 0
    episode = 0
    year = 0
    pixel = 0
    media_type = None

    formatted_name = split_by_first_re_pattern(file_name, [variables.RE_SERIE, variables.RE_YEAR, variables.RE_VIDEO_PIXELS])[0]
    formatted_name = clean_text(formatted_name)
    name_with_metadata = formatted_name

    if match_serie:
        media_type = "tv show"
        #print("Match: ", match_serie[0])
        season, episode = extract_numbers(match_serie[0])
        #print("Hello: ", season, episode)
        #name_with_metadata += "S" + two_digits(season) + "E" + two_digits(episode)
        name_with_metadata += " S" + season + "E" + episode # TODO: fix so they are always 2 digits - 04 not 4.
    else:
        #print("No match: ", match_serie)
        if match_year:
            media_type = "movie"
            year = match_year[0]
            #print("Found Year: ", year)
            name_with_metadata += " (" + year + ")"

        if match_pixel:
            media_type = "movie"
            pixel = match_pixel[0]
            #print("Pixels: ", pixel)
            name_with_metadata += " [" + pixel + "p]"
    #print("YEAR: ", match_year)
    #print("SERIE: ", match_serie)
    #print("PIXEL: ", match_pixel)
    #print(name_with_metadata)
    #print(formatted_name)
    return formatted_name, name_with_metadata, media_type


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
                #print(filename)
                formatted_filename, filename_with_metadata, media_type = format_file_name(filename)
                #print(formatted_filename)
                # From IMDB if I don't like the one from format_file_name()
                #media_type_imdb = media.get_imdb_info(formatted_filename)
                #print(media_type_imdb)
                print(file_path)
                extension = small_functions.get_file_extension(filename)
                print(extension)
                # TODO: Forgot file extention :(
                # And where to move....
                if media_type == "asdasd": # should be movie.
                    print("Creating folder.")
                    new_file_path = os.path.join(folder_path, filename_with_metadata)
                    print("old: ", file_path)
                    print("new: ", new_file_path)
                    small_functions.create_folder(new_file_path)
                    #shutil.move(file_path, new_file_path) # Current to old.


                #print("Name: ", split_by_first_re_pattern(filename, [variables.RE_SERIE, variables.RE_YEAR, variables.RE_VIDEO_PIXELS])[0])
                #print("Video: ", contains_regex(filename, variables.RE_YEAR))
                #print("Serie: ", contains_regex(filename, variables.RE_SERIE)) # checks for 'S01E02' format
                # TODO: Check if movie, serie or else? Preferable by re first then format name

        #print(video_files)

    except Exception as e:
        return str(e)


def main():
    sorter(r"D:\Downloads\2 - Torrents")
    #small_functions.create_folder(r"D:\Desktop Two\test_folder_lol")
"""     if isinstance(movies, list):
        print("Movie files found:")
        for movie in movies:
            print(movie)
    else:
        print("Error:", movies) """


if __name__ == '__main__':
    main()