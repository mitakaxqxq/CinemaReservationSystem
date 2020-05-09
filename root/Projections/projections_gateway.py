from root.db import Database
from .models import ProjectionModel


class ProjectionGateway:
    def __init__(self):
        self.model = ProjectionModel
        self.db = Database()

    def create(self, movie_id, projection_type, date_p, time_p):
        self.db = Database()
        query = '''
        INSERT INTO projections(movie_id, type, date_p, time_p) VALUES(?,?,?,?);
        '''
        self.db.cursor.execute(query, (movie_id, projection_type, date_p, time_p))
        print('Done.')
        self.db.connection.commit()
        self.db.connection.close()

    def select_movie_name_by_its_id(self, movie_id):
        self.db = Database()
        query = '''
        SELECT name FROM movies WHERE id = ?;
        '''
        self.db.cursor.execute(query, (movie_id, ))
        name = self.db.cursor.fetchone()[0]
        self.db.connection.commit()
        self.db.connection.close()
        return name

    def get_projection_by_movie_id(self, movie_id):
        self.db = Database()
        query = '''
        SELECT * FROM projections WHERE movie_id = ? ORDER BY date_p;
        '''

        self.db.cursor.execute(query, (movie_id, ))
        result = self.db.cursor.fetchall()
        self.db.connection.commit()
        self.db.connection.close()
        return result

    def get_movies_dates_by_movie_id(self, movie_id):
        self.db = Database()
        query = '''
        SELECT date_p FROM projections WHERE movie_id = ?;
        '''

        self.db.cursor.execute(query, (movie_id))
        result = self.db.cursor.fetchall()
        self.db.connection.commit()
        self.db.connection.close()
        list_of_dates = []
        for elem in result:
            list_of_dates.append(elem[0])
        return list_of_dates

    def get_projection_by_movie_id_and_date(self, movie_id, date):
        self.db = Database()
        query = '''
        SELECT * FROM projections WHERE movie_id = ? AND date_p like ? ORDER BY date_p;
        '''

        self.db.cursor.execute(query, (movie_id, date))
        result = self.db.cursor.fetchall()
        self.db.connection.commit()
        self.db.connection.close()
        return result

    def all_projections_and_movies_names(self):
        self.db = Database()
        query = f'''
        SELECT name, date_p, time_p, type FROM projections JOIN movies ON projections.movie_id = movies.id;
        '''
        self.db.cursor.execute(query)
        result = self.db.cursor.fetchall()
        self.db.connection.commit()
        self.db.connection.close()
        return result

    def get_information_for_current_projection(self, projection_id):
        self.db = Database()
        query = '''SELECT date_p, time_p, type FROM projections WHERE id = ?;'''
        self.db.cursor.execute(query, (projection_id))
        result = self.db.cursor.fetchone()
        self.db.connection.commit()
        self.db.connection.close()
        return result
