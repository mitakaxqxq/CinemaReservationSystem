from .controllers import UserContoller
from root.Projections.views import ProjectionViews
from root.movies.views import MovieView
from root.Reservations.views import ReservationViews

import os


class UserViews:
    def __init__(self):
        self.controller = UserContoller()

    def login(self):
        username = input('Username: ')
        password = input('Password: ')
        print(list(password))
        result = self.controller.login_user(username=username, password=password)
        user_id = self.get_id(result)
        self.show_list_of_commands(user_id)

    def signup(self):
        username = input('Username: ')
        password = input('Password: ')

        return self.controller.create_user(username=username, password=password)

    def show_list_of_commands(self, user_id):
        all_comanads = ['help', 'show_projections', 'make_reservation', 'show_movies', 'exit', 'sign_out']
        options = f'''
--------------------
1. show_movies
--------------------
2. show_projections
--------------------
3. make_reservation
--------------------
4. help
--------------------
5. sign_out
    '''
        print(options)
        command = input('>Choose command: ')
        while command not in all_comanads:
            command = input('>Incorrect command, choose again: ')
        self.execute_commands(command, user_id)

    def execute_commands(self, command, user_id):
        if command == 'help':
            os.system('clear')
            self.show_help_command(user_id)

        elif command == 'show_projections':
            os.system('clear')
            self.show_projections()
            exit = input('Write exit to return back: ')
            if exit == 'exit':
                os.system('clear')
                self.show_list_of_commands(user_id)

        elif command == 'make_reservation':
            os.system('clear')
            self.make_reservations(user_id)
            os.system('clear')
            self.show_list_of_commands(user_id)
        elif command == 'show_movies':
            os.system('clear')
            self.show_movies()
            exit = input('Write exit to return back: ')
            if exit == 'exit':
                os.system('clear')
                self.show_list_of_commands(user_id)
        elif command == 'sign_out':
            print('Sign out')

    def show_help_command(self, user_id):
        show_help = f'''
---------------------------------------------------------------------------
|     Show Movies     |     Show Projections     |     Make Resrvation    |
---------------------------------------------------------------------------
|   Show all current  |   Show all projections   |   Make reservation for |
|        movies.      |      for all movies.     |    the movie you want  |
|                     |                          |        to watch.       |
---------------------------------------------------------------------------
    '''
        print(show_help)
        exit = input('Write exit to return back: ')
        if exit == 'exit':
            os.system('clear')
            self.show_list_of_commands(user_id)

    def show_movies(self):
        MovieView().get_movies()

    def show_projections(self):
        ProjectionViews().show_all_projections()

    def get_id(self, user):
        return user[0]

    def make_reservations(self, user_id):
        ReservationViews().make_reservation(user_id)
