import os
import sys

import variables
from lib import small_functions

# Import from sorting...

# Check all movies I currently have.
# Save it somewhere. Like a database or whatever.
# From both Movies and Torrent folder.
# Check all movies in here:
# https://www.1377x.to/popular-movies
# If I don't have them
# Check they are not ["TS", "HDTS"] or other cam
# check not hindi
# Check IMDB for rating, "drama, comedy", actors etc.
# check IMDB language is english
# Check if vip_actors is in




def main():
    folders = small_functions.list_folders(r"D:\Videos\Movies")
    for folder in folders:
        print(folder)
    print(variables.LIST_VIP_ACTORS) #variables.


if __name__ == '__main__':
    main()
