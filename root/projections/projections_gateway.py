from root.db import Base, Session
from root.movies.models import MovieModel
from .models import ProjectionModel
from sqlalchemy import desc


class ProjectionGateway:
    def __init__(self):
        self.db = Base()
        self.session = Session()

    def create(self, movie_id, projection_type, date_p, time_p):
        self.session = Session()
        projection = ProjectionModel(movie_id=movie_id, projection_type=projection_type, date_p=date_p, time_p=time_p)
        self.session.add(projection)
        self.session.commit()

        raw_projection = self.session.query(ProjectionModel).filter(
            ProjectionModel.movie_id == movie_id).filter(ProjectionModel.projection_type == projection_type).filter(
            ProjectionModel.date_p == date_p).filter(ProjectionModel.time_p == time_p).one()
        self.session.close()
        return raw_projection

    def select_movie_name_by_its_id(self, movie_id):
        self.session = Session()
        name = self.session.query(MovieModel.title).filter(MovieModel.movie_id == movie_id).one()
        self.session.close()
        return name

    def get_projection_by_movie_id(self, movie_id):
        self.session = Session()
        result = self.session.query(ProjectionModel).filter(ProjectionModel.movie_id == movie_id).all()
        self.session.close()
        return result

    def get_movies_dates_by_movie_id(self, movie_id):
        self.session = Session()
        result = self.session.query(ProjectionModel.date_p).filter(ProjectionModel.movie_id == movie_id).all()
        self.session.close()
        return result

    def get_projection_by_movie_id_and_date(self, movie_id, date):
        self.session = Session()
        result = self.session.query(ProjectionModel).filter(
            ProjectionModel.movie_id == movie_id).filter(
            ProjectionModel.date_p == date).order_by(desc(ProjectionModel.date_p)).all()
        self.session.close()
        return result

    def all_projections_and_movies_names(self):
        self.session = Session()
        result = self.session.query(
            MovieModel.title, ProjectionModel.date_p, ProjectionModel.time_p, ProjectionModel.projection_type).filter(
            MovieModel.movie_id == ProjectionModel.movie_id).all()
        self.session.commit()
        return result

    def get_information_for_current_projection(self, projection_id):
        self.session = Session()
        result = self.session.query(
            ProjectionModel.date_p, ProjectionModel.time_p, ProjectionModel.projection_type).filter(
            ProjectionModel.projection_id == projection_id).one()
        self.session.commit()
        return result
