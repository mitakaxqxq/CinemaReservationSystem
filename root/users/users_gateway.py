from root.db import Database
from .models import UserModel
import os


class UserGateway:
    def __init__(self):
        self.model = UserModel
        self.db = Database()

    def create(self, *, username, password):
        self.db.create_connection()
        self.db.connect_cursor()
        self.model.validate(username, password)

        hashed_password = self.model.hash_password(password)
        query = '''
        INSERT INTO users(username, password) VALUES(?,?);
        '''

        self.db.cursor.execute(query, (username, hashed_password,))
        self.db.connection.commit()
        self.db.connection.close()

        self.db.create_connection()
        self.db.connect_cursor()
        get_query = '''SELECT id FROM users WHERE username = ?'''
        self.db.cursor.execute(get_query, (username,))
        user_id = self.db.cursor.fetchone()[0]
        self.db.connection.commit()
        self.db.connection.close()

        return self.model(id=user_id, username=username, password=hashed_password)

    def login(self, *, username, password):
        self.db.create_connection()
        self.db.connect_cursor()
        get_user_query = '''SELECT * FROM users WHERE username = ?'''
        self.db.cursor.execute(get_user_query, (username,))
        raw_user = self.db.cursor.fetchone()
        self.db.connection.commit()
        self.db.connection.close()

        if raw_user:
            hashed_password = self.model.hash_password(password)
            if hashed_password == raw_user[2]:
                os.system('clear')
                print(f'Welcome, user {raw_user[1]}')
                return raw_user
            else:
                raise ValueError('Wrong password!')
        else:
            raise ValueError('No such user!')
