from .controllers import ProjectionContoller


class ProjectionViews:
    def __init__(self):
        self.controller = ProjectionContoller()

    def get_projection_by_movie_id(self):
        movie_id= input('Choose your movie id: ')
        current_projections = self.controller.get_projection_by_movie_id(movie_id)
        print('Current projection only by movie_id: ')
        for proj in current_projections:
            print(proj)
