from .validations import validate_movie_id, validate_title, validate_rating
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
import sys
sys.path.append('..')


from db import Base


class Movies(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)

    @staticmethod
    def validate(name, rating):
        validate_title(name)
        validate_rating(rating)
