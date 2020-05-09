import sys
from .controllers import ProjectionContoller


class ProjectionViews:
    def __init__(self):
        self.controller = ProjectionContoller()

    def show_all_projections(self):
        all_projections = self.controller.show_all_projections()
        print("           Show all projections             ")
        for proj in all_projections:
            print('--------------------------------------------')
            print(f'''{proj[0]} {proj[1]} {proj[2]} {proj[3]}''')

    def show_projections(self):
        input_choice = input('Choose your movie id or cancel_reservation(write cancel): ')
        if input_choice == 'cancel':
            return input_choice
        movie_id = int(input_choice)
        result = self.controller.get_projection_by_movie_id(movie_id)
        for elem in result:
            print(elem[3], elem[4])
        date = input("Above are the possible dates. If you want to choose date, write the date, if not, press enter. ")
        name = self.controller.select_movie_name_by_its_id(movie_id)
        if date == '':
            current_projections = self.controller.get_projection_by_movie_id(movie_id)
        else:
            current_projections = self.controller.get_projection_by_movie_id_and_date(movie_id, date)
        print(f''' Projections for movie {name}: ''')

        for proj in current_projections:
            print(f'----------------------------------------------')
            print(f'''[{proj[0]}] {proj[3]} {proj[4]} {proj[2]}''')
        return movie_id

    def create(self):
        print("Add new projection of a movie: ")
        movie_id = input("Input movie id here: ")
        date = input("Date of projection: ")
        time = input("Add time of projection: ")
        projection_type = input("Add type of projection (for example 4D, 2D and etc.): ")
        self.controller.create(movie_id, projection_type, date, time)

    def show_movie_name(self, movie_id):
        name = self.controller.select_movie_name_by_its_id(movie_id)
        return name

    def get_inoformation_for_current_projection(self, projection_id):
        info = self.controller.get_information_for_current_projection(projection_id)
        return info
