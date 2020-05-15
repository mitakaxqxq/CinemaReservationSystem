from sqlalchemy import Column, Integer, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship
import sys
sys.path.append('..')


from db import Base
from users.models import UserModel
from projections.models import ProjectionModel


class ReservationModel(Base):
    __tablename__ = 'reservations'
    reservation_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(UserModel.user_id))
    user = relationship(UserModel, backref='reservations')
    projection_id = Column(Integer, ForeignKey(ProjectionModel.projection_id))
    projection = relationship(ProjectionModel, backref='reservations')
    row = Column(Integer, CheckConstraint('row>0 and row<10'))
    col = Column(Integer, CheckConstraint('col>0 and col<10'))
