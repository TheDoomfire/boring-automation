#import hashlib
import requests
import re

# DATADUMP:
# https://dl.opensubtitles.org/addons/export/


""" def verify_subtitle_hash(movie_file, subtitle_url):
    # Calculate the hash value of the movie file
    with open(movie_file, 'rb') as f:
        movie_hash = hashlib.sha1(f.read()).hexdigest()

    # Download the subtitle file
    subtitle_response = requests.get(subtitle_url)
    subtitle_data = subtitle_response.content

    # Calculate the hash value of the subtitle file
    subtitle_hash = hashlib.sha1(subtitle_data).hexdigest()
    print("Movie Hash: ", movie_hash)
    print("Sub Hash: ", subtitle_hash)

    # Compare the hash values
    if movie_hash == subtitle_hash:
        print("Subtitle hash values match. Subtitles are compatible with the movie file.")
    else:
        print("Subtitle hash values do not match. Subtitles are not compatible with the movie file.")
 """

""" def download_subtitle(movie_file, subtitle_url):
    # Calculate the hash value of the movie file
    with open(movie_file, 'rb') as f:
        movie_hash = hashlib.sha1(f.read()).hexdigest()

    # Download the subtitle file
    subtitle_response = requests.get(subtitle_url)
    subtitle_data = subtitle_response.content

    # Calculate the hash value of the subtitle file
    subtitle_hash = hashlib.sha1(subtitle_data).hexdigest()

    # Compare the hash values
    if movie_hash == subtitle_hash:
        # Save the subtitle file
        with open(movie_file.split('.')[0] + '.srt', 'wb') as f:
            f.write(subtitle_data)
        print('Subtitle downloaded successfully.')
    else:
        print('Subtitle hash values do not match. Subtitles are not compatible with the movie file.') """



def subtitle_finder(movie_name):
    with open('D:\Documents\GitHub\boring-automation\sorting\data\subtitles_all.txt', 'r') as f:
        lines = f.readlines()

    # Skip the header line
    lines = lines[1:]

    # Find the line with the matching movie name
    matching_line = [line for line in lines if movie_name in line]

    if matching_line:
        movie_info = matching_line[0].split("\t")
    else:
        return None

    return movie_info



def main():
    # Example usage
    movie_file = r"D:\Downloads\2 - Torrents\Friday The 13Th (2009) [1080p]\Friday.the.13th.2009.1080p.BluRay.x264.YIFY.mp4"
    subtitle_url = "https://www.opensubtitles.org/en/subtitles/5778018/friday-the-13th-en"
    #verify_subtitle_hash(movie_file, subtitle_url)
    movie_name = "Friday The 13Th"
    subtitle_finder(movie_name)


if __name__ == '__main__':
    main()
