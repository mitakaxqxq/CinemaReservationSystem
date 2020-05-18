import unittest
from root.db import Base, Session, engine
from ..models import UserModel
from ..users_gateway import UserGateway

class TestReservationGateway(unittest.TestCase):

    @classmethod
    def setUp(self):
        Base.metadata.create_all(engine)
    
    def test_create_users(self):
        users_gateway = UserGateway()
        result = users_gateway.create(username="Kalin Petrov", password="Malinkat@")
        expected = UserModel(username="Kalin Petrov", password="2a13d86ffeba54a4c5f04f1112e0068818e32812a27cb6bbd7934f60c64fd650")
        self.assertEqual(result, expected)
    

    def test_login(self):
        users_gateway = UserGateway()
        result = users_gateway.login(username="Kalin Petrov", password="Malinkat@")
        expected = UserModel(username="Kalin Petrov", password="2a13d86ffeba54a4c5f04f1112e0068818e32812a27cb6bbd7934f60c64fd650")
        self.assertEqual(result, expected)

    def test_raises_exception_if_it_is_wrong_password(self):
        users_gateway = UserGateway()
        exc = None
        try:
            result = users_gateway.login(username="Kalin Petrov", password="Malinkat@1")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Wrong password!')

    def test_raises_exception_if_it_is_wrong_username(self):
        users_gateway = UserGateway()
        exc = None
        try:
            result = users_gateway.login(username="Kalin Petrovv", password="Malinkat@")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'No row was found for one()')


    @classmethod
    def tearDown(cls):
        session = Session()
        session.query(UserModel).filter(UserModel.user_id == "Kalin Petrov").delete()
        session.commit()
        session.close()
        engine.dispose()


if __name__ == '__main__':
    unittest.main()