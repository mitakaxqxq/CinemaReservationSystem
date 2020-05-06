from .reservations_gateway import ReservationGateway


class ReservationContoller:
    def __init__(self):
        self.reservations_gateway = ReservationGateway()

    def create(self, user_id, projection_id, row, col):
        reservations = self.reservations_gateway.create(user_id, projection_id, row, col)
        return reservations

    def get_rows_and_cols(self, projection_id):
        taken_seats = self.reservations_gateway.get_rows_and_cols(projection_id)
        return taken_seats