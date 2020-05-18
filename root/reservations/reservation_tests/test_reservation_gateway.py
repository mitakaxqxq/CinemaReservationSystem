import unittest
from root.db import Base, Session, engine
from ..models import ReservationModel
from ..reservations_gateway import ReservationGateway

class TestReservationGateway(unittest.TestCase):

    @classmethod
    def setUp(self):
        Base.metadata.create_all(engine)

    def test_add_reservation(self):
        reservation_gateway = ReservationGateway()
        result = reservation_gateway.create(user_id=1, projection_id=7, row=4, col=4)
        expected = ReservationModel(user_id=1, projection_id=7, row=4, col=4)
        self.assertEqual(result, expected)


    @classmethod
    def tearDown(cls):
        session = Session()
        session.query(ReservationModel).filter(ReservationModel.user_id == 7).delete()
        session.commit()
        session.close()
        engine.dispose()
if __name__ == '__main__':
    unittest.main()