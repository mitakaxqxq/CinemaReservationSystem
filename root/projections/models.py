from .validations import *


class ProjectionModel:
    def __init__(self, projection_id, movie_id, projection_type, date_p, time_p):
        validate_date(date_p)
        validate_time(time_p)
        validate_id(projection_id)
        validate_movie_id(movie_id)
        self.id = projection_id
        self.movie_id = movie_id
        self.type = projection_type
        self.date_p = date_p
        self.time_p = time_p
