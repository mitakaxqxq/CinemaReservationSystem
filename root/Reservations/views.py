import sys
from .controllers import ReservationContoller
from .hall import hall
from . utils import print_hall


class ReservationViews:
    def __init__(self):
        self.controller = ReservationContoller()

    def show_available_seats(self, projection_id):
        taken_seats = self.controller.get_rows_and_cols(projection_id)
        current_seats = hall
        for i in range(1, 10):
            for j in range(1, 10):
                create_tuple = (i, j)
                if create_tuple in taken_seats:
                    current_seats[i][j] = '✖'
        print_hall(current_seats)
        return current_seats

    def find_spots(self, projection_id):
        spots = 0
        taken_seats = self.show_available_seats(projection_id)
        for list_seats in taken_seats:
            for seat in list_seats:
                if seat == '✔':
                    spots = spots + 1
        return spots
