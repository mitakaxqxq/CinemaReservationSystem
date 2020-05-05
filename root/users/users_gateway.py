from root.db import Database
from .models import UserModel

class UserGateway:
    def __init__(self):
        self.model = UserModel()
        self.db = Database()

    def create(self, *, username, password):
        self.model.validate(username, password)

        query = '''
        INSERT INTO users(username, password) VALUES(?,?);
        '''

        self.db.cursor.execute(query, (username, password))  # TODO: create user query

        # TODO: What whould I return?
        self.db.connection.commit()
        self.db.connection.close()

    def all(self):
        raw_users = self.db.cursor.execute()  # TODO: Select all users

        return [self.model(**row) for row in raw_users]
