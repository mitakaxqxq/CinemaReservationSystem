from db import Base, Session
from .models import MovieModel


class MovieGateway:
    def __init__(self):
        self.db = Base()
        self.session = Session()

    def add_movie(self, title, rating):
        self.session = Session()
        movie = MovieModel(title, rating)
        self.session.add(movie)
        self.session.commit()

        raw_movie = self.session.query(MovieModel).filter(MovieModel.title == title).filter(MovieModel.rating == rating)
        return raw_movie

    def show_movies(self):
        all_movies = self.session.query(MovieModel.movie_id, MovieModel.title, MovieModel.rating).all()
        return all_movies
