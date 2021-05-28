from sqlalchemy.orm import Session
from .. import models
from .survey_statistics import *
from .keystroke_statistics import *

def gen_statistics(db: Session):
    """
        Generate cumulative statistics
    """

    result = {}

    result['interviewee'] = interviewee_statistics(db)
    result['isPolishNative'] = isPolishNative(db)
    result['hand_preferences'] = hand_preference(db)
    result['sex'] = sex(db)
    result['education'] = education(db)
    result['employment'] = employment(db)
    result['likeScience'] = likeScience(db)
    result['age'] = age(db)

    result['rollover_chart'] = rollover_chart(db)
    result['asit_chart'] = asit_chart(db)
    result['ec_chart'] = ec_chart(db)
    result['enc_chart'] = enc_chart(db)
    result['capsLockUsage_chart'] = capsLockUsage_chart(db)
    result['science_vs_human_asit'] = science_vs_human_asit(db)
    result['left_vs_right_hand_asit'] = left_vs_right_hand_asit(db)
    result['age_vs_enc'] = age_vs_enc(db)
    result['age_vs_asit'] = age_vs_asit(db)
    result['lang_enc'] = lang_enc(db)
    result['lang_ec'] = lang_ec(db)
    result['so_sa_sch'] = so_sa_sch(db)
    result['long_lostalt_invalidcase_other'] = long_lostalt_invalidcase_other(db)
    result['education_vs_asit'] = education_vs_asit(db)
    result['atst_chart'] = atst_chart(db)
    result['rollover_vs_asit'] = rollover_vs_asit(db)
    result['rollover_vs_atst'] = rollover_vs_atst(db)

    return result

def interviewee_statistics(db: Session):
    """
        Return interviewee specific statistics
    """

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
