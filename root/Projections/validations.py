def validate_id(projection_id):
    if not isinstance(projection_id, int):
        return TypeError("Id must be integer!")


def validate_movie_id(movie_id):
    if not isinstance(movie_id, int):
        return TypeError("Id must be integer!")


def validate_time(time_p):
    if not isinstance(time_p, str):
        return TypeError("Time must be string!")
    length = len(time_p)
    if length > 5:
        return ValueError("Time must be in format '00:00'")
    hours = time_p[0] + time_p[1]
    minutes = time_p[3] + time_p[4]

    if int(hours) > 23:
        raise ValueError("Hours must be less than 24!")
    if int(minutes) > 59:
        raise ValueError("Minutes must be less than 60!")


def validate_date(date_p):
    if not isinstance(date_p, str):
        return TypeError("Date must be string!")
