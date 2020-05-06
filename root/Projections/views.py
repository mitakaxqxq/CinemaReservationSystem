import sys
from .controllers import ProjectionContoller


class ProjectionViews:
    def __init__(self):
        self.controller = ProjectionContoller()

    def show_projections(self):
        movie_id = input('Choose your movie id: ')
        date = input("You can choose date if you want: ")

        name = self.controller.select_movie_name_by_its_id(movie_id)
        if date == '':
            current_projections = self.controller.get_projection_by_movie_id(movie_id)
        else:
            current_projections = self.controller.get_projection_by_movie_id_and_date(movie_id, date)
        print(f'''
        ###################################################################
        Projections for movie {name}:
        ###################################################################
        ''')

        for proj in current_projections:
            print(f'''
----------------------------------------------------
[{proj[0]}] {proj[3]} {proj[4]} {proj[2]}
----------------------------------------------------
''')

    def create(self):
        print("Add new projection of a movie: ")
        movie_id = input("Input movie id here: ")
        date = input("Date of projection: ")
        time = input("Add time of projection: ")
        type = input("Add type of projection (for example 4D, 2D and etc.): ")
        self.controller.create(movie_id, type, date, time)
