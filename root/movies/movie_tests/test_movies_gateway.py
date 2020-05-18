import unittest
from ..movies_gateway import MovieGateway
from root.db import Base, Session, engine
from ..models import MovieModel


class TestMovieGateway(unittest.TestCase):

    @classmethod
    def setUp(self):
        Base.metadata.create_all(engine)

    def test_add_movie_method(self):
        movie_gateway = MovieGateway()
        result = movie_gateway.add_movie("Ivan", 7)
        expected = MovieModel(title="Ivan", rating=7)
        self.assertEqual(result, expected)

    def test_show_movies_method(self):
        movie_gateway = MovieGateway()
        movie_gateway.add_movie("Ivan", 7)
        result = movie_gateway.show_movies()
        expected = [MovieModel(title="Ivan", rating=7)]
        self.assertEqual(result, expected)

    @classmethod
    def tearDown(cls):
        session = Session()
        session.query(MovieModel).filter(MovieModel.title == "Ivan").delete()
        session.commit()
        session.close()
        engine.dispose()


if __name__ == '__main__':
    unittest.main()
