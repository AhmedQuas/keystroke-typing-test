from sqlalchemy.orm import Session
from .. import models
from .. helpers.db_mappers import *

def gen_statistics(db: Session):
    """
    
    """

    result = {}

    result['interviewee'] = interviewee_statistics(db)
    result['isPolishNative'] = isPolishNative(db)
    result['hand_preferences'] = hand_preference(db)
    result['sex'] = sex(db)
    
    return result

def interviewee_statistics(db: Session):

    interviewee_id = db.query(models.survey).order_by(models.survey.id.desc()).first().id
    
    interviewee_stats = db.query(models.keystroke_statistic).filter(models.keystroke_statistic.user_id == interviewee_id).first()

    return {
        'rollover': interviewee_stats.rollover,
        'asit': interviewee_stats.asit, 
        'aspt': interviewee_stats.aspt,
        'atst': interviewee_stats.atst,
        'att': interviewee_stats.att,
        'ec': interviewee_stats.ec,
        'enc': interviewee_stats.enc,
        'tfs': interviewee_stats.tfs,
        'sch': interviewee_stats.sch,
        'so': interviewee_stats.so,
        'sa': interviewee_stats.sa,
        'longAlt': interviewee_stats.longAlt,
        'lostAlt': interviewee_stats.lostAlt,
        'invalidCase': interviewee_stats.invalidCase,
        'capsLockUsage': interviewee_stats.capsLockUsage,
    }

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