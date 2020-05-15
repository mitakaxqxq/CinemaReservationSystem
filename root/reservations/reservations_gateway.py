from db import Base, Session
from models import ReservationModel


class ReservationGateway:
    def __init__(self):
        self.db = Base()
        self.session = Session()

    def create(self, user_id, projection_id, row, col):
        self.session = Session()
        reservation = ReservationModel(user_id, projection_id, row, col,)
        self.session.add(reservation)
        raw_reservation = self.session.query(
            ReservationModel.reservation_id).filter(ReservationModel.user_id == user_id).filter(
            ReservationModel.projection_id == projection_id).filter(
            ReservationModel.row == row).filter(ReservationModel.col == col)
        return raw_reservation

    def get_rows_and_cols(self, projection_id):
        self.session = Session()
        taken_seats = self.session.query(ReservationModel.row, ReservationModel.col).filter(
            ReservationModel.projection_id == projection_id)
        return taken_seats


def main():
    pass


if __name__ == '__main__':
    main()
