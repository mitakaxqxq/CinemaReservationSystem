from root.db import Database
from .models import MovieModel
from .movies_queries import *


class MovieGateway:
    def __init__(self):
        self.model = MovieModel
        self.db = Database()

    def add_movie(self, title, rating):
        self.db = Database()
        query = '''
        INSERT INTO movies (title, rating)
        VALUES (?, ?);
        '''
        self.db.cursor.execute(query, (title, rating))
        self.db.connection.commit()
        self.db.connection.close()

        self.db = Database()
        get_movie_by_id_query = '''
        SELECT id
        FROM movies
        WHERE title = ? and rating = ?;'''

        self.db.cursor.execute(get_movie_by_id_query, (title, rating))
        movie_id = self.db.cursor.fetchone()[0]

        self.db.connection.commit()
        self.db.connection.close()
        return self.model(movie_id=movie_id, title=title, rating=rating)

    def show_movies(self):
        self.db = Database()
        self.db.cursor.execute(select_all_movies_and_order_by_rating)
        raw_movies = self.db.cursor.fetchall()

        self.db.connection.commit()
        self.db.connection.close()
        all_movies = []

        for movie in raw_movies:
            new_movie = self.model(movie_id=movie[0], title=movie[1], rating=movie[2])
            all_movies.append(new_movie)

        return raw_movies
