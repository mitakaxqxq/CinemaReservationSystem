def validate_movie_id(movie_id):
    if not isinstance(movie_id, int):
        raise TypeError('Movie id must be of int type!')
    if movie_id < 0:
        raise ValueError('Movie id must be positive!')


def validate_title(title):
    if not isinstance(title, str):
        raise TypeError('Title must be of type str!')


def validate_rating(rating):
    if not isinstance(rating, float):
        raise TypeError('Rating must be of float type!')
    if rating < 0:
        raise ValueError('Rating must be positive!')
