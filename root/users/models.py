import hashlib
from sqlalchemy import Column, String, Integer
from .validations import validate_username, validate_password
from root.db import Base


class UserModel(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    @staticmethod
    def validate_values(username, password):
        validate_username(username)
        validate_password(password)

    def hash_password(password):
        password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        return password
