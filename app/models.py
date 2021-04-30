from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class survey(Base):
    __tablename__ = 'surveys'

    id = Column(Integer, primary_key = True, index = True)
    age = Column(Integer)
    isPolishNative = Column(Boolean)
    sex = Column(Boolean)
    handPreference = Column(Boolean)
    education = Column(Integer)
    employment = Column(Integer)
    likeScience = Column(Boolean)

class test_data(Base):
    __tablename__ = 'test-user-stats'

    id = Column(Integer, primary_key = True, index = True)
