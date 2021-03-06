from .controllers import ReservationController
from .hall import hall
from .utils import print_hall
from root.movies.views import MovieView
from root.projections.views import ProjectionViews
from .colors import f
from root.decorators import log_info


class ReservationViews:
    def __init__(self):
        self.controller = ReservationController()

    def make_reservation(self, user_id):
        tickets = self.start_reservation()
        if tickets == 'cancel':
            return None
        movie_id = self.choose_movie()
        if movie_id == 'cancel':
            return None
        projection_id = self.choose_projection()
        if projection_id == 'cancel':
            return None
        finalize = self.reservating_seats(user_id, movie_id, tickets, projection_id)
        return finalize

    def start_reservation(self):
        print("Let's make your reservation!")
        choice = input("Input number of tickets you want or cancel reservation(write 'cancel'): ")
        tickets = self.string_to_int(choice)
        return tickets

    def choose_movie(self):
        print('You can choose one of these movies: ')
        MovieView().get_movies()
        input_choice = input('Choose your movie id or cancel_reservation(write cancel): ')
        movie_id = self.string_to_int(input_choice)
        return movie_id

    def choose_projection(self):
        ProjectionViews().show_projections()
        projection_id = input("Choose projection_id  or cancel reservation(write 'cancel'): ")
        return projection_id

    def reservating_seats(self, user_id, movie_id, tickets, projection_id):
        self.show_available_seats(projection_id)
        choosen_seats = self.choose_seats(tickets, projection_id)
        i = 0
        self.show_final_reservation(movie_id, projection_id, choosen_seats)
        finalize = input("Input 'finalize' your final reservation or cancel_reservation(write 'cancel'): ")
        if finalize == 'finalize':
            while i < len(choosen_seats) - 1:
                self.controller.create(user_id, projection_id, choosen_seats[i], choosen_seats[i + 1])
                i = i + 2
            self.make_final_reservation(movie_id, projection_id, choosen_seats)
            print('Thanks.')
            answer = input('Do you want to return to main menu - y/n: ')
            if answer == 'y':
                return finalize
        elif finalize == 'cancel':
            return finalize

    def string_to_int(self, value):
        if value == 'cancel':
            return value
        else:
            int_value = int(value)
            return int_value

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
        print("These are your seats: ")
        i = 0
        while i < len(choosen_seats) - 1:
            print(f'({choosen_seats[i]}, {choosen_seats[i+1]})')
            i = i + 2

    @log_info
    def make_final_reservation(self, movie_id, projection_id, choosen_seats):
        name = ProjectionViews().show_movie_name(movie_id)
        info = ProjectionViews().get_inoformation_for_current_projection(projection_id)
        i = 0
        string_of_seats = ""
        while i < len(choosen_seats) - 1:
            print(f'({choosen_seats[i]}, {choosen_seats[i+1]})')
            string_of_seats += f'({choosen_seats[i]}, {choosen_seats[i+1]})'
            string_of_seats += ' '
            i = i + 2
        return f'Name of movie: {name} Date and time: {info[0]} - {info[1]} - {info[2]} Seats: {string_of_seats}'
