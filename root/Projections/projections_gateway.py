from root.db import Database
from .models import ProjectionModel


class ProjectionGateway:
    def __init__(self):
        self.model = ProjectionModel
        self.db = Database()

    def create(self, id, movie_id, type, date_p, time_p):
        query = '''
        INSERT INTO projections(movie_id, type, date_p, time_p) VALUES(?,?,?,?,?);
        '''

        self.db.cursor.execute(query, (id, movie_id, type, date_p, time_p))
        self.db.connection.commit()
        self.db.connection.close()


    def get_projection_by_movie_id(self, movie_id):
        query = '''
        SELECT * FROM projections WHERE movie_id = ? ORDER BY date_p;
        '''
        self.db.cursor.execute(query, (movie_id, ))
        result = self.db.cursor.fetchall()
        print(result)

        self.db.connection.commit()
        self.db.connection.close()
        return result

    def get_projection_by_movie_id_and_date(self, movie_id, date):

        query = '''
        #SELECT * FROM projections WHERE movie_id = ? AND date_p like ? ORDER BY date_p;
        '''

        self.db.cursor.execute(query, (movie_id, date))
        self.db.connection.commit()
        self.db.connection.close()


def main():
    pass

if __name__ == '__main__':
    main()