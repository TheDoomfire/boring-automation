import re
from series import extract_season_episode
import imdb


# TODO: get movie name, and format it nice?
# Return "movie_file_name" or "movie_name"
def get_movie_name(file_name):
    # Define a regular expression pattern to match movie names
    # Examples: "movie name (2013) [720p]" or "strange.world.2022.1080p.webrip.hevc.x265.rmteam"
    pattern = re.compile(r'^(.+?)(?:\s*\(\d{4}\))?[\s\.\[\(_]*(?:\d{3,4}p)?.*$')

    # Use the pattern to match and extract the movie name
    match = pattern.match(file_name)
    
    if match:
        print("Match: ", match)
        return match.group(1).strip()
    else:
        return None
    
def is_movie(file_name):
    # Check format movie name (year) [pixels]
    #movie_name = get_movie_name(file_name)
    ia = imdb.IMDb()
    # Using the Search movie method
    movies = ia.search_movie(file_name)
    # Check is not serie
    # Grab the name
    # Check IMDB database
    #print(items)
    movie = movies[0]
    ia.update(movie, info=["taglines", "trivia"])

    print(movie["rating"])


def get_imdb_info(movie_name):
    try:
        # Create an instance of the IMDb class
        ia = imdb.IMDb()

        # Search for the movie using the provided name
        movies = ia.search_movie(movie_name)

        # Check if there are any results
        if len(movies) == 0:
            return None

        # Check if there's an exact match
        exact_match = False
        for movie in movies:
            if movie['title'].lower() == movie_name.lower():
                exact_match = True
                break

        # Get the movie rating
        rating = None
        if exact_match:
            movie_id = movie.movieID
            movie = ia.get_movie(movie_id)
            rating = movie['rating']
            media_type = movie.get('kind', 'movie') # "movie" or "tv show"
            year = movie['year']

        return media_type, rating
    except:
        return None


def main():
    print(get_media_type("Gladiator"))
    print(get_movie_name("PAW.Patrol.The.Mighty.Movie.2023.1080p.AMZN.WEB-DL.DDP5.1.Atmos.H.264-FLUX"))


if __name__ == '__main__':
    main()