import os
import re
import shutil

# Custom Imports
import variables # On main app gets the error "no module named 'variables'"
import subtitle
from checking import media
from lib import small_functions


# TODO: Make one for LAST re pattern. To find possibly uploaders
def split_by_first_re_pattern(input_string, patterns):
    for pattern in patterns:
        match = re.search(pattern, input_string)
        if match:
            return re.split(pattern, input_string, maxsplit=1)
    # If no pattern is found, return the original string
    return [input_string]


def split_by_last_re_pattern(input_string, patterns):
    last_match = None
    for pattern in patterns:
        match = re.search(pattern, input_string)
        if match:
            last_match = match

    if last_match:
        return re.split(last_match.re.pattern, input_string, maxsplit=1)

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


def remove_leading_zeros(input_str):
    # Use the int() function to convert the input string to an integer,
    # and then convert it back to a string to remove leading zeros
    result_str = str(int(input_str))
    return result_str


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

    season = None
    episode = None
    year = None
    pixel = None
    media_type = None

    formatted_name = split_by_first_re_pattern(file_name, [variables.RE_SERIE, variables.RE_YEAR, variables.RE_VIDEO_PIXELS])[0]
    file_name_release_group = split_by_last_re_pattern(file_name, [variables.RE_SERIE, variables.RE_YEAR, variables.RE_VIDEO_PIXELS])[-1]
    formatted_name = clean_text(formatted_name)
    name_with_metadata = formatted_name

    # To try and get the name
    # .BrRip.x264.YIFY
    # .HULU.WEBRip.800MB.x264-GalaxyRG
    # .NF.WEBRip.800MB.x264-GalaxyRG
    # .BluRay.DD5.1.x264-GalaxyRG[TGx]
    # .WEBRip.1600MB.DD5.1.x264-GalaxyRG[TGx]
    # .1080p.AMZN.WEBRip.1400MB.DD5.1.x264-GalaxyRG
    #splitted = small_functions.split_by_this( file_name_release_group, ".")

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
    return formatted_name, name_with_metadata, media_type, year, file_name_release_group, season



def sorter(folder_path):
    video_files = []
    try:
    # Check if the folder path exists
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")
        
        # Iterate through files in the folder
        for root, _, files in os.walk(folder_path):
            for filename in files:
                file_path = os.path.join(root, filename)
        #for filename in os.listdir(folder_path):
            #file_path = os.path.join(folder_path, filename)
            
                # Check if the file is a regular file and has a video extension
                if os.path.isfile(file_path) and any(file_path.lower().endswith(ext) for ext in variables.EXTENSION_VIDEOS):
                    video_files.append(file_path)
                    video_file_extension, video_file_name_without_extension = small_functions.get_file_extension(filename)
                    #print(filename)
                    #formatted_filename, filename_with_metadata, media_type, media_year = format_file_name(filename)
                    the_formatted_file_name = format_file_name(filename)
                    formatted_filename = the_formatted_file_name[0]
                    filename_with_metadata = the_formatted_file_name[1]
                    media_type = the_formatted_file_name[2]
                    media_year = the_formatted_file_name[3]
                    season = the_formatted_file_name[5]
                    has_subtitle = None
                    #print(formatted_filename)
                    # From IMDB if I don't like the one from format_file_name()
                    #media_type_imdb = media.get_imdb_info(formatted_filename)
                    #print(media_type_imdb)
                    #extension = small_functions.get_file_extension(filename)
                    if media_type == "movie": # should be movie.
                        print("Is movie.")
                        movie_path = small_functions.get_file_path(file_path)
                        new_file_path = os.path.join(variables.PATH_MOVIES, filename_with_metadata)
                        new_file_path_with_file = os.path.join(new_file_path, filename)
                        print("---------- Creating folder ----------")
                        small_functions.create_folder(new_file_path)
                        if movie_path == folder_path:
                            print("No subfolder: ", movie_path)
                            print(file_path)
                            print(new_file_path_with_file)
                            shutil.move(file_path, new_file_path_with_file)
                        else:
                            print("SUBFOLDER")
                            print(movie_path)
                            print(new_file_path)
                            #print(small_functions.file_has_subtitles(file_path)) # DONT WORK!
                            for root, _, files in os.walk(movie_path):
                                print("---------- LOOKING FOR FILES ----------")
                                for file in files:
                                    print("FILE: ", file) 
                                    the_file_path = os.path.join(movie_path, file)
                                    #print(file.lower().endswith(".mp4"))
                                    # TODO: if files exist in new folder, then delete it.

                                    if any(file.lower().endswith(ext) for ext in variables.EXTENSION_SUBTITLES):
                                        print("FOUND SUBTITLE")
                                        subtitle_extension = small_functions.get_file_extension(file)[0]
                                        new_subtitle_file_name = video_file_name_without_extension + subtitle_extension
                                        new_subtitle_file_path = os.path.join(new_file_path, new_subtitle_file_name)
                                        shutil.move(the_file_path, new_subtitle_file_path)
                                        has_subtitle = True
                                    else:
                                        print("NOT FOUND SUBTITLE")
                                        # TODO:
                                        # If already exists that file
                                        # Then delete it.
                                        # Check if the file exists at the new location
                                        if os.path.exists(new_file_path_with_file):
                                            print("EXISTS", new_file_path)
                                            # If it exists, delete it
                                            #os.remove(the_file_path)
                                            print("DELETE THIS?: ", new_file_path_with_file)
                                            print("file_path: ", file_path)
                                        else:
                                            shutil.move(the_file_path, new_file_path)
                                    print(the_file_path)
                        if has_subtitle == None:
                            print("Folder HAD NO SUBTITLES :(")
                            print("Find and downloading subtitles...")
                            print("Filename: ", filename)
  
                            print("Trying to download the file.....")
                            subtitle.find_and_download_subtitle(filename, new_file_path)
                            print("Downloaded subtitles.")

                            # TODO: Need to rename the subtitle file.
                            new_subtitles = small_functions.find_subtitle_files(new_file_path)
                            new_subtitle = new_subtitles[0]

                            subtitle_extension = small_functions.get_file_extension(new_subtitle)[0]
                            new_subtitle_file_name = video_file_name_without_extension + subtitle_extension
                            
                            old_subtitle_path = os.path.join(new_file_path, new_subtitle)
                            new_subtitle_file_path = os.path.join(new_file_path, new_subtitle_file_name)
                            print("-------------------------------")
                            print("OLD SUB: ", old_subtitle_path)
                            print("NEW SUB: ", new_subtitle_file_path)
                            print("-------------------------------")

                            shutil.move(old_subtitle_path, new_subtitle_file_path)
                            has_subtitle = True

                            print("Now it has a subtitle file!!")

                            small_functions.delete_empty_folders(movie_path)
                    elif media_type == "tv show":
                        serie_path = small_functions.get_file_path(file_path)
                        serie_season_folder = "Season " + remove_leading_zeros(season)
                        serie_season_folder_path = os.path.join(variables.PATH_SERIES, formatted_filename, serie_season_folder)
                        new_serie_path_with_file = os.path.join(serie_season_folder_path, filename)

                        small_functions.create_folder(serie_season_folder_path)
                        if serie_path == folder_path:
                            print("No subfolder")
                            print(file_path)
                            print(new_serie_path_with_file)
                            shutil.move(file_path, new_serie_path_with_file)
                            # TODO: Check if has subtitle
                            # Get subtitle
                            # Rename subtitle
                            #if has_subtitle == None:
                                #subtitle.find_and_download_subtitle(filename, serie_season_folder_path)
                        else:
                            print("")
                            print("------ Subfolder -----")
                            for root, _, files in os.walk(serie_path):
                                for file in files:
                                    old_path = os.path.join(serie_path, file)
                                    new_path = os.path.join(serie_season_folder_path, file)
                                    print(filename)
                                    print(old_path)
                                    print(new_path)
                                    # TODO: If new_path already exists
                                    shutil.move(old_path, new_path)
                                    # TODO: If subtile found

                        small_functions.delete_empty_folders(serie_path)


                #print("Name: ", split_by_first_re_pattern(filename, [variables.RE_SERIE, variables.RE_YEAR, variables.RE_VIDEO_PIXELS])[0])
                #print("Video: ", contains_regex(filename, variables.RE_YEAR))
                #print("Serie: ", contains_regex(filename, variables.RE_SERIE)) # checks for 'S01E02' format
                # TODO: Ignore temp folder?
                # Stop seeding torrent?

        #print(video_files)

    except Exception as e:
        return str(e)


def main():
    # TODO: Add counter showing all movies that where moved.

    sorter(r"D:\Downloads\2 - Torrents")
    #sorter(r"G:\Downloads")

    # Problems

    #small_functions.create_folder(r"D:\Desktop Two\test_folder_lol")
"""     test_list = ["Rumble.Through.the.Dark.2023.1080p.AMZN.WEBRip.1400MB.DD5.1.x264-GalaxyRG",
                 "She.Came.to.Me.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG[TGx]",
                 "Sisu.2023.1080p.AMZN.WEBRip.1400MB.DD5.1.x264-GalaxyRG[TGx]",
                 "SOUTH.PARK.JOINING.THE.PANDERVERSE.2023.1080p.WEB.H264-HUZZAH[TGx]",
                 "The.Burial.2023.1080p.WEBRip.1400MB.DD5.1.x264-GalaxyRG[TGx]",
                 "Zombie.Town.2023.720p.WEBRip.800MB.x264-GalaxyRG",
                 "Friday.the.13th.2009.1080p.BluRay.x264.YIFY",
                 "A.Nightmare.on.Elm.Street.2010.1080p.BrRip.x264.BOKUTOX.YIFY.mkv-muxed"
                 ]
    for item in test_list:
        format_file_name(item) """


if __name__ == '__main__':
    main()