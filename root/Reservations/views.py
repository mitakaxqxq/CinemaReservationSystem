import os
from .controllers import ReservationContoller
from .hall import hall
from .utils import print_hall
from root.movies.views import MovieView
from root.Projections.views import ProjectionViews
from .colors import f


class ReservationViews:
    def __init__(self):
        self.controller = ReservationContoller()

    def make_reservation(self, user_id):
        command = ''
        print("Let's make your reservation!")
        choice = input("Input number of tickets you want or cancel reservation(write 'cancel'): ")
        if choice == 'cancel':
            return choice
        tickets = int(choice)

        print('You can choose one of these movies: ')
        MovieView().get_movies()
        movie_id = ProjectionViews().show_projections()
        if movie_id == 'cancel':
            return movie_id

        projection_id_choice = input("Choose projection_id  or cancel reservation(write 'cancel'): ")
        if projection_id_choice == 'cancel':
            return projection_id_choice
        projection_id = projection_id_choice
        self.show_available_seats(projection_id)

        choosen_seats = self.choose_seats(tickets, projection_id)
        i = 0
        self.show_final_reservation(movie_id, projection_id, choosen_seats)

        finalize = input("Input 'finalize' your final reservation or cancel_reservation(write 'cancel'): ")
        if finalize == 'finalize':
            while i < len(choosen_seats) - 1:
                result = self.controller.create(user_id, projection_id, choosen_seats[i], choosen_seats[i + 1])
                i = i + 2
            print('Thanks.')
            answer = input('Do you want to return to main menu - y/n: ')
            if answer == 'y':
                return finalize
        elif finalize == 'cancel':
            return finalize

    def show_available_seats(self, projection_id):
        taken_seats = self.controller.get_rows_and_cols(projection_id)
        current_seats = hall
        for i in range(1, 10):
            for j in range(1, 10):
                create_tuple = (i, j)
                if create_tuple in taken_seats:
                    current_seats[i][j] = f'{f.r}✖{f.e}'
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
        choosen_seats = []
        while i <= tickets:
            print(f'Choose your seat {i}: ')
            row = int(input(f'Choose row: '))
            col = int(input(f'Choose column: '))
            result = self.check_if_it_is_taken_or_invalid(row, col, projection_id)
            while result is not True:
                row = int(input(f'Choose row: '))
                col = int(input(f'Choose column: '))
                result = self.check_if_it_is_taken_or_invalid(row, col, projection_id)
            choosen_seats.append(row)
            choosen_seats.append(col)
            i = i + 1
        return choosen_seats

    def check_if_it_is_taken_or_invalid(self, row, col, projection_id):
        taken_seats = self.controller.get_rows_and_cols(projection_id)
        tup = (row, col)
        if tup in taken_seats:
            print('This seat is taken!')
            return False
        elif row >= 11 or col >= 11:
            print('There are only 10 rows and 10 columns!')
            return False
        else:
            return True

    def show_final_reservation(self, movie_id, projection_id, choosen_seats):
        print("This is your reservation:")
        name = ProjectionViews().show_movie_name(movie_id)
        print(f'Movie name: {name} ')
        info = ProjectionViews().get_inoformation_for_current_projection(projection_id)
        print(f"Date and time: {info[0]} - {info[1]} - {info[2]}")
        print("This is your seats: ")
        i = 0
        while i < len(choosen_seats) - 1:
            print(f'({choosen_seats[i]}, {choosen_seats[i+1]})')
            i = i + 2
