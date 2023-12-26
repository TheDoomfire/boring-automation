import os
from lib import small_functions
#from sorting import format_file_name
import sorting


# TODO: It's very slow... Need to find out why.
def subtitle_finder(file_name):
    # TODO: Make this work with any location like "\sorting\data\subtitles_all.txt"
    # Otherwise very hard to work in other computers.
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

    exact_name_match = None
    with open(subtitle_file, 'r', encoding='utf-8') as file:
        count = -1
        best_match = None
        best_id = 0
        for line in file:
            # Skip the header line
            if not line.startswith('IDSubtitle'):
                # Split the line using tab as a delimiter
                data = line.strip().split('\t')
                # Check if the line has enough elements
                #print(len(data))
                if len(data) > 3:
                    # Extract the MovieName and LanguageName from the line
                    current_movie_name = small_functions.remove_special_characters(data[1].lower())
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
    return { 'download_url': best_download_url, 'exact_name': exact_name_match, 'best_match': best_match, 'result': result }


def find_and_download_subtitle(file_name, download_path):
    # TODO: Downloads new file if movie_name not found?
    # https://dl.opensubtitles.org/addons/export/subtitles_all.txt.gz
    # or if subtitle_finder() returns nothing?

    # Looks for the subtitles
    found_subtitles = subtitle_finder(file_name)
    result = found_subtitles['result']
    if not result:
        print("Not found")
    else:
        print("Found!")

    download_url = found_subtitles['download_url']

    # Downloads it
    small_functions.download_file(download_url, download_path)

    # Finds the file
    archived_files = small_functions.find_archive_files(download_path)
    archived_file = archived_files[0]
    archived_file_path = os.path.join(download_path, archived_file)
    small_functions.unzip_file(archived_file_path, download_path)


def mass_download_opensub_data():
    print("hey")



def main():
    #subtitle_file = r'D:\Documents\GitHub\boring-automation\sorting\data\subtitles_all.txt'
    movie_file = r"D:\Downloads\2 - Torrents\Friday The 13Th (2009) [1080p]\Friday.the.13th.2009.1080p.BluRay.x264.YIFY.mp4"
    subtitle_url = "https://www.opensubtitles.org/en/subtitles/5778018/friday-the-13th-en"
    #verify_subtitle_hash(movie_file, subtitle_url)
    #movie_name = "Friday The 13Th"
    #movie_name = "Friday.the.13th.2009.1080p.BluRay.x264.YIFY"
    #test_movie_name = "loki.s02e05.1080p.web.h264-lazycunts"
    download_path = r"D:\Desktop Two\test"
    #test_movie_name = "Ricky.Gervais.Armageddon.2023.1080p.WEB.h264-ETHEL[TGx]" # Dosen't exist in file
    test_movie_name = "Batman Begins (2005) 1080p BluRay x264 - 1.6GB - YIFY" # Does exist in file
    test_var = subtitle_finder(test_movie_name)
    result = test_var['result']
    print("--- TEST_VAR ---")
    print(test_var['result'])
    if not result:
        print("Not found.")
    else:
        print("Movie found!")

    #print(subtitle_finder(test_movie_name))
    # find_and_download_subtitle()


if __name__ == '__main__':
    main()
