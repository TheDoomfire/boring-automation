""" def subtitle_finder(movie_name):
    subtitle_file = r'D:\Documents\GitHub\boring-automation\sorting\data\subtitles_all.txt'
    result = []
    with open(subtitle_file, 'r', encoding='utf-8') as file:
        for line in file:
            # Skip the header line
            if not line.startswith('IDSubtitle'):
                # Split the line using tab as a delimiter
                data = line.strip().split('\t')
                # Check if the line has enough elements
                if len(data) > 1:
                    # Extract the MovieName from the line
                    current_movie_name = data[1]
                    # Check if the specified movie_name is present in the current line
                    if movie_name.lower() in current_movie_name.lower():
                        result.append(line.strip())
    return result
 """

from sorting import sorting


# TODO:
# Try to find a exact MovieReleaseName = filename without the extension
# Otherwise, compare the hash of all?
# Just takes one.
# find the uploaders name? or blueray etc.
# MovieYear
def subtitle_finder(file_name):
    subtitle_file = r'D:\Documents\GitHub\boring-automation\sorting\data\subtitles_all.txt' # TODO: Make this work with any lockation like "\sorting\data\subtitles_all.txt"
    result = []
    # TODO: Make it work with just file name
    # And it takes the year and movie name.
    # If year dosent exist it looks in IMDB for it.
    file_name_formating = sorting.format_file_name(file_name)
    movie_name = file_name_formating[0]
    with open(subtitle_file, 'r', encoding='utf-8') as file:
        for line in file:
            # Skip the header line
            if not line.startswith('IDSubtitle'):
                # Split the line using tab as a delimiter
                data = line.strip().split('\t')
                # Check if the line has enough elements
                if len(data) > 3:
                    # Extract the MovieName and LanguageName from the line
                    current_movie_name = data[1].lower()
                    language_name = data[3].lower()
                    # Check if the specified movie_name is present in the current line
                    # (exact match, lowercase)
                    # and if the language is English
                    if movie_name.lower() == current_movie_name and language_name == 'english':
                        result.append(line.strip())
    return result


def main():
    #subtitle_file = r'D:\Documents\GitHub\boring-automation\sorting\data\subtitles_all.txt'
    movie_file = r"D:\Downloads\2 - Torrents\Friday The 13Th (2009) [1080p]\Friday.the.13th.2009.1080p.BluRay.x264.YIFY.mp4"
    subtitle_url = "https://www.opensubtitles.org/en/subtitles/5778018/friday-the-13th-en"
    #verify_subtitle_hash(movie_file, subtitle_url)
    movie_name = "Friday The 13Th"
    movie_name = "Friday The 13Th"
    #print(subtitle_finder(movie_name)[0])


if __name__ == '__main__':
    main()
