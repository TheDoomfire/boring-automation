import os

from ..sorting import variables

# Check all movies I currently have.
# From both Movies and Torrent folder.
# Check all movies in here:
# https://www.1377x.to/popular-movies
# If I don't have them
# Check they are not ["TS", "HDTS"] or other cam
# check not hindi
# Check IMDB for rating, "drama, comedy", actors etc.
# check IMDB language is english
# Check if vip_actors is in


def list_folders(directory):
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    return folders


def main():
    folders = list_folders(r"D:\Videos\Movies")
    for folder in folders:
        print(folder)
    print(variables.LIST_VIP_ACTORS)


if __name__ == '__main__':
    main()
