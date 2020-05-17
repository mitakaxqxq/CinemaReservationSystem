import sys
from root.db import *
from root.initializer import insert_into_movies, insert_into_projections, insert_into_reservations, insert_into_users
from root.index_view import welcome


class Application:
    @classmethod
    def build(self):
        Base.metadata.create_all(engine)
        insert_into_movies()
        insert_into_projections()
        insert_into_reservations()
        insert_into_users()
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
