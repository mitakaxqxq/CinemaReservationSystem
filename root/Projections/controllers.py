from .projections_gateway import ProjectionGateway


class ProjectionContoller:
    def __init__(self):
        self.projections_gateway = ProjectionGateway()

    def get_projection_by_movie_id(self, movie_id):
        projections = self.projections_gateway.get_projection_by_movie_id(movie_id=movie_id)
        return projections

    def get_projection_by_movie_id_and_date(self, movie_id, date):
        projections = self.projections_gateway.get_projection_by_movie_id_and_date(movie_id=movie_id, date=date)
        return projections

    def select_movie_name_by_its_id(self, movie_id):
        projections = self.projections_gateway.select_movie_name_by_its_id(movie_id)
        return projections

    def create(self, movie_id, type, date, time):
        self.projections_gateway.create(movie_id, type, date, time)

    def show_all_projections(self):
        all_projections = self.projections_gateway.all_projections_and_movies_names()
        return all_projections
