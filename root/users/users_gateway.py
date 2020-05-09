from root.db import Database
from .models import UserModel
import os

class UserGateway:
    def __init__(self):
        self.model = UserModel
        self.db = Database()

    def create(self, *, username, password):
        self.db = Database()
        self.model.validate(username, password)

        hashed_password = self.model.hash_password(password)

        query = '''
        INSERT INTO users(username, password) VALUES(?,?);
        '''

        self.db.cursor.execute(query, (username, hashed_password))
        self.db.connection.commit()
        self.db.connection.close()

        self.db = Database()
        get_query = f'SELECT id FROM users WHERE username = "{username}"'
        self.db.cursor.execute(get_query)
        user_id = self.db.cursor.fetchone()[0]
        self.db.connection.commit()
        self.db.connection.close()

        return self.model(id=user_id, username=username, password=hashed_password)

    def login(self, *, username, password):
        self.db = Database()
        get_user_query = f'SELECT * FROM users WHERE username = "{username}"'
        self.db.cursor.execute(get_user_query)
        raw_user = self.db.cursor.fetchone()
        self.db.connection.commit()
        self.db.connection.close()

        if raw_user:
            hashed_password = self.model.hash_password(password)
            if hashed_password == raw_user[2]:
                os.system('clear')
                print(f'Welcome, user {raw_user[1]}')
                self.model(id=raw_user[0], username=raw_user[1], password=raw_user[2])
                return raw_user
            else:
                raise ValueError('Wrong password!')
        else:
            raise ValueError('No such user!')

