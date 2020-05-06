import unittest
import sys

sys.path.append('..')

from validations import validate_username, validate_password


class TestValidateNicknameFunction(unittest.TestCase):
    def test_raises_exception_when_character_in_username_is_not_in_allowed_symbols(self):
        exc = None
        try:
            validate_username("{vanko09")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Username character { is not in allowed symbols!')


class TestValidatePasswordFunction(unittest.TestCase):
    def test_raises_exception_when_length_of_password_is_less_than_eight_symbols(self):
        exc = None
        try:
            validate_password("vanko09")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Password length must be at least 8 symbols!')

    def test_raises_exception_when_no_capital_symbol_in_password(self):
        exc = None
        try:
            validate_password("vanko009")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Password must contain at least 1 capital symbol!')

    def test_raises_exception_when_no_special_symbol_in_password(self):
        exc = None
        try:
            validate_password("Vanko009")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Password must contain at least 1 special symbol!')


if __name__ == '__main__':
    unittest.main()
