import os
from lib import small_functions
#from sorting import format_file_name
import sorting
import variables # name 'variables' is not defined ???
from configparser import ConfigParser
from datetime import date


# TODO: It's very slow... Need to find out why.
def subtitle_finder(file_name):
    print("--- Running: subtitle_finder ---")
    # TODO: Make this work with any location like "\sorting\data\subtitles_all.txt"
    # Otherwise very hard to work in other computers.
    #print("--- Running: subtitle_finder ---")
    subtitle_file = r'D:\Documents\GitHub\boring-automation\sorting\data\subtitles_all.txt' 
    result = []
    # TODO: Make it work with just file name
    # And it takes the year and movie name.
    # If year doesn't exist it looks in IMDB for it.
    # get_file_extension()
    file_name_formating = sorting.format_file_name(file_name)
    movie_file_name = file_name_formating[0].lower()
    movie_file_year = file_name_formating[3]
    file_name_release_group = file_name_formating[4]
    #file_name_release_group = small_functions.split_by_this_and_remove_single_chars(file_name_release_group, ".")
    file_name_release_group = small_functions.split_by_these_and_remove_single_chars(file_name_release_group, [".", " "])

    print("Movie File Name: ", movie_file_name)
    print("Movie File Year: ", movie_file_year)
    print("file_name_release_group: ", file_name_release_group)

    exact_name_match = None
    with open(subtitle_file, 'r', encoding='utf-8') as file:
        #print("Opening file!")
        count = -1
        best_match = None
        best_id = 0
        for line in file:
            #print("For every line.")
            # Skip the header line
            if not line.startswith('IDSubtitle'):
                #print("not line.startswith('IDSubtitle')")
                # Split the line using tab as a delimiter
                data = line.strip().split('\t')
                # Check if the line has enough elements
                #print(len(data))
                if len(data) > 3:
                    #print("len(data) > 3")
                    # Extract the MovieName and LanguageName from the line
                    current_movie_name = small_functions.remove_special_characters(data[1].lower())
                    #print(current_movie_name) # ERROR: NOT SHOWING???
                    id = data[0]
                    movie_year = data[2].lower()    
                    language_name = data[3].lower()
                    #series_season = data[11] #list index out of range
                    #print(series_season)
                    #series_episode = data[12]
                    # Check if the specified movie_name is present in the current line
                    # (exact match, lowercase)
                    # and if the language is English

                    # ImdbID data[5], check it if it's a serie?


                    if movie_file_name == current_movie_name and language_name == 'english' and movie_file_year == movie_year:
                        #print("English") # NOT SHOWING!!
                        #print("---------------------------")
                        #print(file_name)
                        movie_release_name = data[9].lower() # IndexError: list index out of range
                        #print(movie_release_name)
                        url = data[15].lower()
                        # TODO: Make it split more then dots. Also spaces.
                        #movie_release_name_splitted = small_functions.split_by_this_and_remove_single_chars(movie_release_name, ".")
                        movie_release_name_splitted = small_functions.split_by_these_and_remove_single_chars(movie_release_name, [" ", "."])
                        #movie_release_name_splitted = movie_release_name.split(".")
                        count_matches = small_functions.count_common_elements(file_name_release_group, movie_release_name_splitted)
                        #print("Count: ", count_matches)
                    
                        if movie_release_name == file_name:
                            exact_name_match = url
                            
                        if count < count_matches:
                            count = count_matches
                            best_match = url
                            best_id = id

                        result.append(line.strip())

    if best_id:
        best_download_url = "https://www.opensubtitles.org/subtitleserve/sub/" + str(best_id)
    else:
        best_download_url = None
        
    # result, exact_name_match, best_match, best_id, best_download_url
    print(result)
    return { 'download_url': best_download_url, 'exact_name': exact_name_match, 'best_match': best_match, 'result': result }


def find_and_download_subtitle(file_name, download_path):
    print("Running: find_and_download_subtitle")
    # TODO: Downloads new file if movie_name not found?
    # https://dl.opensubtitles.org/addons/export/subtitles_all.txt.gz
    # or if subtitle_finder() returns nothing?

    # Looks for the subtitles
    found_subtitles = subtitle_finder(file_name)

    result = found_subtitles['result']
    #print(found_subtitles) # taking forever

    # Checks if it found any result
    if not result:
        print("Not found sub")
        # TODO: Limit the downloading?
        # Store what date it downloaded last time, and check that time against today.
        config = ConfigParser()
        config.read("settings.ini")
        config_data = config["DEFAULT"]
        last_subtitle_update = config_data["last_subtitle_update"]
        today = date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        print(formatted_date)
        print(last_subtitle_update)
        if formatted_date == last_subtitle_update:
            print("The dates are equal.")
        else:
            print("The dates are not equal.")

        if last_subtitle_update != formatted_date:
            print("Not Found sub Again!!!!")
            path_all_subtitles = r"D:\Documents\GitHub\boring-automation\sorting\data" #variables.PATH_ALL_SUBTITLES
            mass_download_opensubtitles_data(path_all_subtitles)
            found_subtitles = subtitle_finder(file_name)
            #small_functions.update_settings_file("DEFAULT", "last_subtitle_download", formatted_date) # Doesn't work??

    else:
        print("Found!")

    download_url = found_subtitles['download_url']
    print("Download URL: ", download_url)

    # Downloads it
    small_functions.download_file(download_url, download_path)

    # Finds the file
    archived_files = small_functions.find_archive_files(download_path)
    archived_file = archived_files[0]
    archived_file_path = os.path.join(download_path, archived_file)
    small_functions.unzip_file(archived_file_path, download_path)



def mass_download_opensubtitles_data(download_path):
    print("--- Running: mass_download_opensubtitles_data ---")
    # Downloads it
    small_functions.download_file_and_replace(variables.URL_ALL_SUBTITLES, download_path)

    # Unzips it
    zip_file_path = os.path.join(variables.PATH_ALL_SUBTITLES, variables.NAME_ALL_SUBTITLE_ZIP)
    small_functions.unzip_file(zip_file_path, download_path)



def main():
    #subtitle_file = r'D:\Documents\GitHub\boring-automation\sorting\data\subtitles_all.txt'
    movie_file = r"D:\Downloads\2 - Torrents\Friday The 13Th (2009) [1080p]\Friday.the.13th.2009.1080p.BluRay.x264.YIFY.mp4"
    subtitle_url = "https://www.opensubtitles.org/en/subtitles/5778018/friday-the-13th-en"
    #verify_subtitle_hash(movie_file, subtitle_url)
    #movie_name = "Friday The 13Th"
    #movie_name = "Friday.the.13th.2009.1080p.BluRay.x264.YIFY"
    #test_movie_name = "loki.s02e05.1080p.web.h264-lazycunts"
    test_movie_name = "Ricky.Gervais.Armageddon.2023.1080p.WEB.h264-ETHEL[TGx]" # Dosen't exist in file
    test_movie_name = "Rebel.Moon.Part.One.A.Child.of.Fire.2023.1080p.WEBRip.x265-KONTRAST.mp4" # WONT WORK??? No subtitle.
    #test_movie_name = "Batman Begins (2005) 1080p BluRay x264 - 1.6GB - YIFY" # Does exist in file

    #find_and_download_subtitle(test_movie_name, "nada")'
    download_path = variables.PATH_ALL_SUBTITLES
    print("Download Path: ", download_path)
    #mass_download_opensubtitles_data(download_path)
    print("Done.")


if __name__ == '__main__':
    main()
