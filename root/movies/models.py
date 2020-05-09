from .validations import validate_movie_id, validate_title, validate_rating


class MovieModel:
    def __init__(self, *, movie_id, title, rating):
        validate_movie_id(movie_id)
        validate_title(title)
        validate_rating(rating)
        self.id = movie_id
        self.title = title
        self.rating = rating
