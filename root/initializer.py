from root.movies.models import MovieModel
from root.users.models import *
from root.projections.models import *
from root.reservations.models import *
from root.db import Session


def insert_into_movies():
    print("Adding new movies to the database via the session object")
    session = Session()
    session.add_all([
        MovieModel(title="The Hunger Games: Catching Fire", rating=7.9),
        MovieModel(title="Wreck-It Ralph", rating=7.8),
        MovieModel(title="Her", rating=8.3)])
    session.commit()
    session.close()


def insert_into_projections():
    print("Adding new projections to the database via the session object")
    session = Session()
    session.add_all([
        ProjectionModel(movie_id=1, projection_type="3D", date_p="2020-04-01", time_p="19:10"),
        ProjectionModel(movie_id=1, projection_type="2D", date_p="2020-04-01", time_p="19:00"),
        ProjectionModel(movie_id=1, projection_type="4DX", date_p="2020-04-02", time_p="21:00"),
        ProjectionModel(movie_id=3, projection_type="2D", date_p="2020-04-05", time_p="20:20"),
        ProjectionModel(movie_id=2, projection_type="3D", date_p="2020-04-02", time_p="22:00"),
        ProjectionModel(movie_id=2, projection_type="2D", date_p="2020-04-02", time_p="19:30")])
    session.commit()
    session.close()


def insert_into_users():
    print("Adding new users to the database via the session object")
    session = Session()
    session.add_all([
        UserModel(username="Kalin Petrov", password="2a13d86ffeba54a4c5f04f1112e0068818e32812a27cb6bbd7934f60c64fd650"),
        UserModel(username="Ivan Ivanov", password="8b2b146e58694903084e0a510e7ce302fee3cef6b9defbd87100777d76d278b7"),
        UserModel(username="Georgi Budov", password="281807ba64ef115395e9980211f069690b5422a78459ef31f15142a41b826ade"),
        UserModel(
            username="Petar Dimitrov", password="868a7dc455e3bcab3a8e66eb16e04c16fef756d043b183b2a07eda0dda6185c5")])
    session.commit()
    session.close()


def insert_into_reservations():
    print("Adding new reservations to the database via the session object")
    session = Session()
    session.add_all([
        ReservationModel(user_id=3, projection_id=1, row=2, col=1),
        ReservationModel(user_id=3, projection_id=1, row=3, col=5),
        ReservationModel(user_id=3, projection_id=1, row=7, col=8),
        ReservationModel(user_id=2, projection_id=3, row=1, col=1),
        ReservationModel(user_id=2, projection_id=3, row=1, col=2),
        ReservationModel(user_id=5, projection_id=5, row=2, col=3),
        ReservationModel(user_id=6, projection_id=5, row=2, col=4)])
    session.commit()
    session.close()
