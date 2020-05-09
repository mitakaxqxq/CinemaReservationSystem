from .controllers import MovieController


class MovieView:
    def __init__(self):
        self.controller = MovieController()

    def get_movies(self):
        all_movies = self.controller.show_all_movies()
        print("             All Movies             ")
        for movie in all_movies:
            print('------------------------------------------')
            print(f'''[{movie[0]}] {movie[1]} {movie[2]}''')
