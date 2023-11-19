import imdb


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
        media_type = None
        year = None
        language = None

        if exact_match:
            movie_id = movie.movieID
            selected_movie = ia.get_movie(movie_id)
            rating = selected_movie['rating']
            media_type = selected_movie.get('kind', 'movie')  # "movie" or "tv show"
            year = selected_movie['year']
            language = ', '.join(selected_movie.get('languages', []))
            countries = selected_movie.get('countries', [])
            genres = ', '.join(selected_movie.get('genres', []))

            # Check if the movie is animated
            animation_department = selected_movie.get('animation department', [])

        return media_type, rating, year, language, countries, genres, animation_department
    except:
        return None
    

def main():
    print(get_imdb_info("Gladiator"))


if __name__ == '__main__':
    main()