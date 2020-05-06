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
