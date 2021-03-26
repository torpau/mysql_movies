from data.db import session
from data.models.movies import Movie, Genre


def store_movies(lines):
    for line in lines:
        # del line['genres']
        line['genres'] = [Genre(genre_name=genre) for genre in line['genres']]
        movie = Movie(**line)
        session.add(movie)
    session.commit()


def get_movie_by_id(_id):
    return session.query(Movie).filter(Movie.movie_id == _id).first()
