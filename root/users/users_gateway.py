from models import UserModel
import os
from db import Database, Session


class UserGateway:
    def __init__(self):
        self.db = Database()
        self.session = Session()

    def create(self, *, username, password):
        self.session = Session()
        UserModel.validate(username, password)

        hashed_password = UserModel.hash_password(password)
        user = UserModel(username=username, password=hashed_password)
        self.session.add(user)
        self.session.commit()

        raw_user = self.session.query(UserModel).filter(UserModel.username == username)
        return raw_user

    def login(self, *, username, password):
        self.session = Session()
        raw_user = self.session.query(UserModel).filter(UserModel.username == username).filter(UserModel.password == UserModel.hash_password(password))
        return raw_user
