from .projections_gateway import ProjectionGateway


class ProjectionContoller:
    def __init__(self):
        self.projections_gateway = ProjectionGateway()

    def get_projection_by_movie_id(self, movie_id):
        projections = self.projections_gateway.get_projection_by_movie_id(movie_id=movie_id)
        return projections
