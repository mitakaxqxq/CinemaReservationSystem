import unittest
from ..projections_gateway import ProjectionGateway
from root.db import Base, Session, engine
from ..models import ProjectionModel
from root.movies.models import MovieModel


class TestProjectionGateway(unittest.TestCase):

    @classmethod
    def setUp(cls):
        Base.metadata.create_all(engine)
        session = Session()
        session.add(MovieModel(title="The Hunger Games: Catching Fire", rating=7.9))
        session.add(MovieModel(title="Wreck-It Ralph", rating=7.8))
        session.add(ProjectionModel(movie_id=1, projection_type="3D", date_p="2020-04-01", time_p="19:10"))
        session.add(ProjectionModel(movie_id=1, projection_type="2D", date_p="2020-04-01", time_p="19:00"))
        session.add(ProjectionModel(movie_id=2, projection_type="2D", date_p="2020-04-01", time_p="19:00"))
        session.commit()

    def test_create_method(self):
        projection_gateway = ProjectionGateway()
        result = projection_gateway.create(1, "4D", "2020-04-02", "19:10")
        expected = ProjectionModel(movie_id=1, projection_type="4D", date_p="2020-04-02", time_p="19:10")
        self.assertEqual(result, expected)

    def test_select_movie_name_by_its_id_method(self):
        projection_gateway = ProjectionGateway()
        result = projection_gateway.select_movie_name_by_its_id(1)[0]
        expected = "The Hunger Games: Catching Fire"
        self.assertEqual(result, expected)

    def test_get_projection_by_movie_id_method(self):
        projection_gateway = ProjectionGateway()
        result = projection_gateway.get_projection_by_movie_id(1)
        expected = [ProjectionModel(movie_id=1, projection_type="3D", date_p="2020-04-01", time_p="19:10"),
                    ProjectionModel(movie_id=1, projection_type="2D", date_p="2020-04-01", time_p="19:00")]
        self.assertEqual(result, expected)

    def test_get_movies_dates_by_movie_id_method(self):
        projection_gateway = ProjectionGateway()
        result = projection_gateway.get_movies_dates_by_movie_id(1)
        expected = [("2020-04-01",), ("2020-04-01",)]
        self.assertEqual(result, expected)

    def test_get_projection_by_movie_id_and_date_method(self):
        projection_gateway = ProjectionGateway()
        result = projection_gateway.get_projection_by_movie_id_and_date(1, "2020-04-01")
        expected = [ProjectionModel(movie_id=1, projection_type="3D", date_p="2020-04-01", time_p="19:10"),
                    ProjectionModel(movie_id=1, projection_type="2D", date_p="2020-04-01", time_p="19:00")]
        self.assertEqual(result, expected)

    def test_all_projections_and_movie_names_method(self):
        projection_gateway = ProjectionGateway()
        result = projection_gateway.all_projections_and_movies_names()
        expected = [("The Hunger Games: Catching Fire", "2020-04-01", "19:10", "3D"),
                    ("The Hunger Games: Catching Fire", "2020-04-01", "19:00", "2D"),
                    ("Wreck-It Ralph", "2020-04-01", "19:00", "2D")]
        self.assertEqual(result, expected)

    def test_get_information_for_current_projection_method(self):
        projection_gateway = ProjectionGateway()
        result = projection_gateway.get_information_for_current_projection(2)
        expected = ("2020-04-01", "19:00", "2D")
        self.assertEqual(result, expected)

    @classmethod
    def tearDown(cls):
        session = Session()
        session.query(MovieModel).delete()
        session.query(ProjectionModel).delete()
        session.commit()
        session.close()
        engine.dispose()


if __name__ == '__main__':
    unittest.main()
