import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_similarity(movies):

    descriptions = [m["overview"] for m in movies]

    vectorizer = TfidfVectorizer(stop_words="english")

    matrix = vectorizer.fit_transform(descriptions)

    similarity = cosine_similarity(matrix)

    return similarity