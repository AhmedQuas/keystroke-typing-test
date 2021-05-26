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
    rollover = Column(Integer)
    asit = Column(Integer)          #Average Sign Time
    aspt = Column(Integer)          #Average Space Time
    atst = Column(Integer)          #Average Tap Space Time
    att = Column(Float)             #Average Tap Time
    tfs = Column(Integer)           #Taps for sign
    capsLockUsage = Column(Boolean)
    ec = Column(Integer)              #Errors Corrected
    enc = Column(Integer)             #Errors Not Corrected
    sch = Column(Integer)             #Sign change
    so = Column(Integer)              #Sign ommission
    sa = Column(Integer)              #Sign addtion
    longAlt = Column(Integer)
    lostAlt = Column(Integer)
    invalidCase = Column(Integer)

    interviewee_keystrokes = relationship('survey', back_populates = 'interviewee_survey')