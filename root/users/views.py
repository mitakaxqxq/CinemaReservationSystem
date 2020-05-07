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
        result = self.controller.login_user(username=username, password=password)

        self.show_list_of_commands()

    def signup(self):
        username = input('Username: ')
        password = input('Password: ')

        return self.controller.create_user(username=username, password=password)

    def show_list_of_commands(self):
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
        self.execute_commands(command)

    def execute_commands(self, command):
        if command == 'help':
            os.system('clear')
            self.show_help_command()

        elif command == 'show_projections':
            os.system('clear')
            self.show_projections()
            exit = input('Write exit to return back: ')
            if exit == 'exit':
                os.system('clear')
                self.show_list_of_commands()

        elif command == 'make_reservation':
            os.system('clear')
            self.make_reservations()

        elif command == 'show_movies':
            os.system('clear')
            self.show_movies()
            exit = input('Write exit to return back: ')
            if exit == 'exit':
                os.system('clear')
                self.show_list_of_commands()
        elif command == 'sign_out':
            print('Sign out')

    def show_help_command(self):
        show_help = f'''
---------------------------------------------------------------------------
|     Show Movies     |     Show Projections     |     Make Resrvation    |
---------------------------------------------------------------------------
|Show all current     |   Show all projections   |   Make reservation for |
|     movies .        |      for all movies.     |     movie you want to  |
|                     |                          |           watch.       |
---------------------------------------------------------------------------
    '''
        print(show_help)
        exit = input('Write exit to return back: ')
        if exit == 'exit':
            os.system('clear')
            self.show_list_of_commands()

    def show_movies(self):
        MovieView().get_movies()

    def show_projections(self):
        ProjectionViews().show_all_projections()

    def make_reservations(self):
        ReservationViews().make_reservation()
