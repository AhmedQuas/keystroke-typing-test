from sqlalchemy.orm import Session
from .. import models
from .. helpers.db_mappers import *

def isPolishNative(db: Session):
    
    yes = db.query(models.survey).filter(models.survey.isPolishNative == m_isPolishNative['yes']).count()
    no = db.query(models.survey).filter(models.survey.isPolishNative == m_isPolishNative['no']).count()

    return {
        'yes': yes,
        'no': no
    }

def hand_preference(db: Session):

    left_hand = db.query(models.survey).filter(models.survey.handPreference == m_handPreference['left']).count()
    right_hand = db.query(models.survey).filter(models.survey.handPreference == m_handPreference['right']).count()


    return {
        'left_hand': left_hand,
        'right_hand': right_hand
    }

def sex(db: Session):
    
    women = db.query(models.survey).filter(models.survey.sex == m_sex['woman']).count()
    men = db.query(models.survey).filter(models.survey.sex == m_sex['man']).count()

    return {
        'women': women,
        'men': men
    }

def education(db: Session):

    primary = db.query(models.survey).filter(models.survey.education == m_education['primary']).count()
    high = db.query(models.survey).filter(models.survey.education == m_education['high']).count()
    student = db.query(models.survey).filter(models.survey.education == m_education['student']).count()
    graduate = db.query(models.survey).filter(models.survey.education == m_education['graduate']).count()
    undergraduate = db.query(models.survey).filter(models.survey.education == m_education['undergraduate']).count()

    return {
        'primary' : primary,
        'high' : high,
        'student' : student,
        'graduate' : graduate,
        'undergraduate' : undergraduate
    }

def employment(db: Session):

    unemployed = db.query(models.survey).filter(models.survey.employment == m_employment['unemployed']).count()
    withcomputer = db.query(models.survey).filter(models.survey.employment == m_employment['withcomputer']).count()
    withoutcomputer = db.query(models.survey).filter(models.survey.employment == m_employment['withoutcomputer']).count()

    return {
        'unemployed': unemployed,
        'withcomputer': withcomputer,
        'withoutcomputer': withoutcomputer
    }

def likeScience(db: Session):

    yes = db.query(models.survey).filter(models.survey.likeScience == m_likeScience['yes']).count()
    no = db.query(models.survey).filter(models.survey.likeScience == m_likeScience['no']).count()

    return {
        'yes': yes,
        'no': no
    }