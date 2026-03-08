import requests

API_KEY = "94342781151f5d57f707732bb9ee5be4"

def search_movie(movie_name):

    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"

    response = requests.get(url)

    data = response.json()

    return data["results"]


def get_similar_movies(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/similar?api_key={API_KEY}"

    response = requests.get(url)

    data = response.json()

    return data["results"]


def get_movie_poster(poster_path):

    base_url = "https://image.tmdb.org/t/p/w500"

    if poster_path:
        return base_url + poster_path

    return None