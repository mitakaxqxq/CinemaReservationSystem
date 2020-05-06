from root.db import Database
from .models import ProjectionModel


class ProjectionGateway:
    def __init__(self):
        self.model = ProjectionModel
        self.db = Database()

    def create(self, movie_id, type, date_p, time_p):
        query = '''
        INSERT INTO projections(movie_id, type, date_p, time_p) VALUES(?,?,?,?);
        '''
        self.db.cursor.execute(query, (movie_id, type, date_p, time_p))
        print('Done.')
        self.db.connection.commit()

    def select_movie_name_by_its_id(self, movie_id):
        query = '''
        SELECT name FROM movies WHERE id = ?;
        '''

        self.db.cursor.execute(query, (movie_id, ))
        name = self.db.cursor.fetchone()[0]
        self.db.connection.commit()
        return name

    def get_projection_by_movie_id(self, movie_id):
        query = '''
        SELECT * FROM projections WHERE movie_id = ? ORDER BY date_p;
        '''

        self.db.cursor.execute(query, (movie_id, ))
        result = self.db.cursor.fetchall()
        self.db.connection.commit()
        return result

    def get_projection_by_movie_id_and_date(self, movie_id, date):

        query = f'''
        SELECT * FROM projections WHERE movie_id = {movie_id} AND date_p like {date} ORDER BY date_p;
        '''

        self.db.cursor.execute(query)
        result = self.db.cursor.fetchall()
        self.db.connection.commit()
        return result


def main():
    pass

if __name__ == '__main__':
    main()