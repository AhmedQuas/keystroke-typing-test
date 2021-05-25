from sqlalchemy.orm import Session
from .. import models
from .survey_statistics import *

def gen_statistics(db: Session):
    """
    
    """

    result = {}

    result['interviewee'] = interviewee_statistics(db)
    result['isPolishNative'] = isPolishNative(db)
    result['hand_preferences'] = hand_preference(db)
    result['sex'] = sex(db)
    result['education'] = education(db)
    result['employment'] = employment(db)
    result['likeScience'] = likeScience(db)

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