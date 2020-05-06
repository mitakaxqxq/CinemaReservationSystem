from root.db import Database
from .models import ReservationModel


class ReservationGateway:
    def __init__(self):
        self.model = ReservationModel
        self.db = Database()

    def create(self, user_id, projection_id, row, col):
        query = '''
        INSERT INTO reservations(user_id, projection_id, row, col) VALUES(?,?,?,?);
        '''
        self.db.cursor.execute(query, (user_id, projection_id, row, col))
        print('Done.')
        self.db.connection.commit()

    def get_rows_and_cols(self, projection_id):
        query = '''
        SELECT row, col FROM reservations WHERE projection_id = ?;
        '''
        self.db.cursor.execute(query, (projection_id,))
        taken_seats = self.db.cursor.fetchall()
        self.db.connection.commit()
        return taken_seats


def main():
    pass


if __name__ == '__main__':
    main()
