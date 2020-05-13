from root.db import Database
from .models import ReservationModel


class ReservationGateway:
    def __init__(self):
        self.model = ReservationModel
        self.db = Database()

    def create(self, user_id, projection_id, row, col):
        self.db.create_connection()
        self.db.connect_cursor()

        query = '''
        INSERT INTO reservations(user_id, projection_id, row, col) VALUES(?,?,?,?);
        '''
        self.db.cursor.execute(query, (user_id, projection_id, row, col,))
        print('Done.')
        self.db.connection.commit()
        self.db.connection.close()

        self.db.create_connection()
        self.db.connect_cursor()
        get_query = '''SELECT id FROM reservations WHERE user_id = ? AND projection_id = ? AND row = ? AND col = ?'''
        self.db.cursor.execute(get_query, (user_id, projection_id, row, col,))
        reservation_id = self.db.cursor.fetchone()[0]
        self.db.connection.commit()
        self.db.connection.close()

        return self.model(id=reservation_id, user_id=user_id, projection_id=projection_id, row=row, col=col)

    def get_rows_and_cols(self, projection_id):
        self.db.create_connection()
        self.db.connect_cursor()

        query = '''
        SELECT row, col FROM reservations WHERE projection_id = ?;
        '''
        self.db.cursor.execute(query, (projection_id,))
        taken_seats = self.db.cursor.fetchall()
        self.db.connection.commit()
        self.db.connection.close()
        return taken_seats


def main():
    pass


if __name__ == '__main__':
    main()
