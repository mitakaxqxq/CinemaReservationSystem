from .models import MovieModel
from root.db import Base, Session


class MovieGateway:
    def __init__(self):
        self.db = Base()
        self.session = Session()

    def add_movie(self, title, rating):
        self.session = Session()
        movie = MovieModel(title=title, rating=rating)
        self.session.add(movie)
        self.session.commit()

        raw_movie = self.session.query(MovieModel).filter(
            MovieModel.title == title).filter(MovieModel.rating == rating).one()
        self.session.close()
        return raw_movie

    def show_movies(self):
        self.session = Session()
        all_movies = self.session.query(MovieModel).all()
        self.session.close()
        return all_movies
