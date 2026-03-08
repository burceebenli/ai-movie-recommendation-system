import streamlit as st
from recommender import recommend
from movie_api import get_movie_poster

st.title("AI Movie Recommendation System")

movie = st.text_input("Enter a movie")

if st.button("Recommend"):

    results = recommend(movie)

    for film in results:

        poster = get_movie_poster(film["poster_path"])

        st.subheader(film["title"])

        if poster:
            st.image(poster)

        st.write(film["overview"])