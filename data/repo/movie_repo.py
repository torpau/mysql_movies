from data.db import session
from data.models.movies import Movie


def store_movies(lines):
    for line in lines:
        del line['genres']
        movie = Movie(**line)
        session.add(movie)
    session.commit()
