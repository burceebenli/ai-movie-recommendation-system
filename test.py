from movie_api import search_movie, get_similar_movies

movies = search_movie("Inception")

movie_id = movies[0]["id"]

similar_movies = get_similar_movies(movie_id)

for movie in similar_movies:
    print(movie["title"])