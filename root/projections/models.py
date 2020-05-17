from .validations import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from root.db import Base
from root.movies import MovieModel


class ProjectionModel(Base):
    __tablename__ = 'projections'
    projection_id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey(MovieModel.movie_id))
    movie = relationship(MovieModel, backref='projections')
    projection_type = Column(String)
    date_p = Column(String)
    time_p = Column(String)

    @staticmethod
    def validate_values(projection_id, movie_id, date_p, time_p):
        validate_id(projection_id)
        validate_movie_id(movie_id)
        validate_date(date_p)
        validate_time(time_p)
