import sys
from root.db import Database
from root.db_schema import CREATE_USERS, CREATE_PROJECTIONS, CREATE_RESERVATIONS, CREATE_MOVIES
from root.db_schema.database_queries import insert_into_movies, insert_into_projections, insert_into_reservations, insert_into_users
from root.index_view import welcome


class Application:
    @classmethod
    def build(self):
        db = Database()
        db.cursor.execute(CREATE_USERS)
        db.cursor.execute(CREATE_RESERVATIONS)
        db.cursor.execute(CREATE_PROJECTIONS)
        db.cursor.execute(CREATE_MOVIES)
        db.cursor.execute(insert_into_movies)
        db.cursor.execute(insert_into_projections)
        db.cursor.execute(insert_into_reservations)
        db.cursor.execute(insert_into_users)
        # TODO: Build rest of the tables
        # TODO: Seed with inistial data - consider using another command for this

        db.connection.commit()
        db.connection.close()

        print('Done.')

    @classmethod
    def start(self):
        while True:
            welcome()


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.start()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
