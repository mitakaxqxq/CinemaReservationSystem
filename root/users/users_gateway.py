from .models import UserModel
import os
from root.db import Base, Session


class UserGateway:
    def __init__(self):
        self.db = Base()
        self.session = Session()

    def create(self, *, username, password):
        self.session = Session()
        UserModel.validate(username, password)

        hashed_password = UserModel.hash_password(password)
        user = UserModel(username, hashed_password)
        self.session.add(user)
        self.session.commit()

        raw_user = self.session.query(UserModel).filter(UserModel.username == username)
        return raw_user

    def login(self, *, username, password):
        self.session = Session()
        raw_user = self.session.query(UserModel).filter(UserModel.username == username).one()
        if raw_user:
            hashed_password = UserModel.hash_password(password)
            result = self.session.query(UserModel.password).filter(UserModel.username == username).one()
            if hashed_password == result[0]:
                os.system('clear')
                print(f'Welcome, user {raw_user.username}')
                return raw_user
            else:
                raise ValueError('Wrong password!')
        else:
            raise ValueError('No such user!')
