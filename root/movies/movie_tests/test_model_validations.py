import unittest
from ..validations import validate_movie_id, validate_rating, validate_title


class TestMovieIDValidation(unittest.TestCase):
    def test_raises_exception_when_movie_id_is_not_of_type_int(self):
        exc = None
        try:
            validate_movie_id(19.2)
        except Exception as err:
            exc = err
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Movie id must be of int type!')

    def test_raises_exception_when_movie_id_is_not_positive_int(self):
        exc = None
        try:
            validate_movie_id(-19)
        except Exception as err:
            exc = err
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Movie id must be positive!')


class TestMovieTitleValidation(unittest.TestCase):
    def test_raises_exception_when_title_is_not_of_type_str(self):
        exc = None
        try:
            validate_title(12)
        except Exception as err:
            exc = err
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Title must be of type str!')


class TestMovieRatingValidation(unittest.TestCase):
    def test_raises_exception_when_rating_is_not_of_type_float(self):
        exc = None
        try:
            validate_rating(19)
        except Exception as err:
            exc = err
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Rating must be of float type!')

    def test_raises_exception_when_rating_is_not_positive_float(self):
        exc = None
        try:
            validate_rating(-19.4)
        except Exception as err:
            exc = err
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Rating must be positive!')


if __name__ == '__main__':
    unittest.main()
