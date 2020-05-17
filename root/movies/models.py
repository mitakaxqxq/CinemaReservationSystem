from .validations import validate_title, validate_rating
from sqlalchemy import Column, Integer, String, Float
import sys
sys.path.append('..')


from root.db import Base


class MovieModel(Base):
    __tablename__ = 'movies'
    movie_id = Column(Integer, primary_key=True)
    title = Column(String)
    rating = Column(Float)

    @staticmethod
    def validate(name, rating):
        validate_title(name)
        validate_rating(rating)
