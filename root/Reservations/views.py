import sys
from .controllers import ReservationContoller
from .hall import hall
from .utils import print_hall
from root.movies.views import MovieView

class ReservationViews:
    def __init__(self):
        self.controller = ReservationContoller()


    def make_reservation(self):
        print("Let's make your reservation!")
        tickets = int(input('Input number of tickets you want: '))
        print('You can choose one of these movies: ')
        MovieView().get_movies()
        projection_id = input('Choose projection_id: ')
        self.show_available_seats(projection_id)
        self.choose_seats(tickets, projection_id)

    def show_available_seats(self, projection_id):
        taken_seats = self.controller.get_rows_and_cols(projection_id)
        current_seats = hall
        for i in range(1, 10):
            for j in range(1, 10):
                create_tuple = (i, j)
                if create_tuple in taken_seats:
                    current_seats[i][j] = '✖'
        print_hall(current_seats)

    def find_spots(self, projection_id):
        spots = 0
        taken_seats = self.show_available_seats(projection_id)
        for list_seats in taken_seats:
            for seat in list_seats:
                if seat == '✔':
                    spots = spots + 1
        return spots

    def choose_seats(self, tickets, projection_id):
        i = 1
        while i <= tickets:
            print(f'Choose your seat {i}: ')
            row = input(f'Choose row: ')
            col = input(f'Choose column: ')
            self.check_if_it_is_taken_or_invalid(row, col, projection_id)
            i = i + 1

    def check_if_it_is_taken_or_invalid(self, row, col, projection_id):
        taken_seats = self.controller.get_rows_and_cols(projection_id)
        tup = (row, col)
        if tup in taken_seats:
            print('Choose another seat: ')
