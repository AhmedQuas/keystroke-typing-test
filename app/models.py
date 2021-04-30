from sqlalchemy import Column, Integer ,String
from .database import Base

class survey(Base):
    __tablename__ = 'surveys'

    id = Column(Integer, primary_key = True, index = True)
    q1 = Column(String(32))
    q2 = Column(String(32))

class test_data(Base):
    __tablename__ = 'test-user-stats'

    id = Column(Integer, primary_key = True, index = True)
