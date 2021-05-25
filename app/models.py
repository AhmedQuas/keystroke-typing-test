from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from .database import Base
from sqlalchemy.orm import relationship

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

    interviewee_survey = relationship('keystroke_statistic', back_populates = 'interviewee_keystrokes')

class keystroke_statistic(Base):
    __tablename__ = 'keystroke_statistics'

    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey('surveys.id'))
    rollover = Column(Float)
    asit = Column(Integer)          #Average Sign Time
    aspt = Column(Integer)          #Average Space Time
    atst = Column(Integer)          #Average Tap Space Time
    att = Column(Float)             #Average Tap Time
    tfs = Column(Integer)           #Taps for sign
    capsLockUsage = Column(Boolean)
    ec = Column(Float)              #Errors Corrected
    enc = Column(Float)             #Errors Not Corrected
    sch = Column(Float)             #Sign change
    so = Column(Float)              #Sign ommission
    sa = Column(Float)              #Sign addtion
    longAlt = Column(Float)
    lostAlt = Column(Float)
    invalidCase = Column(Float)

    interviewee_keystrokes = relationship('survey', back_populates = 'interviewee_survey')