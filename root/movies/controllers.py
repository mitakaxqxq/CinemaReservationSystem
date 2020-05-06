from .movies_gateway import MovieGateway


class MovieController:

    def __init__(self):
        self.gateway = MovieGateway()

    def add_movie(self, title, rating):
        return self.gateway.add_movie(title, rating)

    def show_all_movies(self):
        return self.gateway.show_all_movies()
