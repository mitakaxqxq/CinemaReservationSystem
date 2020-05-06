from .validations import *


class ProjectionModel:
    def __init__(self, id, movie_id, type, date_p, time_p):
        validate_date(date_p)
        validate_time(time_p)
        validate_id(id)
        validate_movie_id(movie_id)
        self.id = id
        self.movie_id = movie_id
        self.type = type
        self.date_p = date_p
        self.time_p = time_p
