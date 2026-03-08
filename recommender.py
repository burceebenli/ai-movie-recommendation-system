from movie_api import search_movie, get_similar_movies

def recommend(movie_name):

    movies = search_movie(movie_name)

    if len(movies) == 0:
        return []

    movie_id = movies[0]["id"]

    similar_movies = get_similar_movies(movie_id)

    return similar_movies[:5]