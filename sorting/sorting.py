import os
from ..lib import variables

def sort_movies(folder_path):
    print("Sorting movies")
    movie_files = []

    try:
        # Check if the folder path exists
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")
        
        # Iterate through files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # Check if the file is a regular file and has a video extension
            if os.path.isfile(file_path) and any(file_path.lower().endswith(ext) for ext in variables.EXTENSION_VIDEOS):
                movie_files.append(file_path)

        return movie_files

    except Exception as e:
        return str(e)
    

def main():
    movies = sort_movies(r"D:\Downloads\2 - Torrents")
    if isinstance(movies, list):
        print("Movie files found:")
        for movie in movies:
            print(movie)
    else:
        print("Error:", movies)


if __name__ == '__main__':
    main()