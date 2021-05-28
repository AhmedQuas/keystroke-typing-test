from app.statistics.survey_statistics import likeScience
from sqlalchemy.orm import Session
from sqlalchemy import func
import math
from .. import models
from .. helpers.db_mappers import *

def rollover_chart(db: Session):
    
    rollover = db.query(models.keystroke_statistic).filter(models.keystroke_statistic.rollover > 0 ).count()
    no_rollover = db.query(models.keystroke_statistic).filter(models.keystroke_statistic.rollover == 0).count()

    return {
        'rollover': rollover,
        'no_rollover': no_rollover
    }

def hist_plot(column, db: Session):

    Xmin = db.query(func.min(column)).scalar()
    Xmax = db.query(func.max(column)).scalar()
    n = db.query(column).count()

    distance = Xmax - Xmin

    #Number of gaps
    #k = math.ceil(1.33 * math.log(n,10))
    k = math.ceil(math.sqrt(n))

    #Gap size
    h = math.ceil(distance/k)

    response = {
        'label': [],
        'amount': []
    }

    val = Xmin

    while val <= Xmax:
        val += h
        response['label'].append(str(val-h) + ' - ' + str(val))
        amount = db.query(column).filter(column.between(val-h,val)).count()
        response['amount'].append(amount)
        val += 1

    return response

def asit_chart(db: Session):

    return hist_plot(models.keystroke_statistic.asit, db)

def atst_chart(db: Session):

    return hist_plot(models.keystroke_statistic.atst, db)

def enc_chart(db: Session):

    return hist_plot(models.keystroke_statistic.enc, db)

def ec_chart(db: Session):

    return hist_plot(models.keystroke_statistic.ec, db)

def capsLockUsage_chart(db: Session):

    capsLockUsage = db.query(models.keystroke_statistic).filter(models.keystroke_statistic.capsLockUsage == True ).count()
    shift = db.query(models.keystroke_statistic).filter(models.keystroke_statistic.capsLockUsage == False).count()

    return {
        'capsLock': capsLockUsage,
        'shift': shift
    }

def science_vs_human_asit(db: Session):

    survey = models.survey
    keystroke = models.keystroke_statistic

    like_science = db.query(func.avg(keystroke.asit)).filter(keystroke.user_id == survey.id).filter(survey.likeScience == m_likeScience['yes']).first()

    like_human = db.query(func.avg(keystroke.asit)).filter(keystroke.user_id == survey.id).filter(survey.likeScience == m_likeScience['no']).first()

    return{
        'likeScience': like_science[0],
        'likeHuman': like_human[0]
    }

def left_vs_right_hand_asit(db: Session):

    survey = models.survey
    keystroke = models.keystroke_statistic

    left = db.query(func.avg(keystroke.asit)).filter(keystroke.user_id == survey.id).filter(survey.handPreference == m_handPreference['left']).first()

    right = db.query(func.avg(keystroke.asit)).filter(keystroke.user_id == survey.id).filter(survey.handPreference == m_handPreference['right']).first()

    return{
        'left': right[0],
        'right': left[0]
    }

def vs_plot(x_axis, y_axis, db: Session):

    survey = models.survey
    keystroke = models.keystroke_statistic

    Xmin = db.query(func.min(x_axis)).scalar()
    Xmax = db.query(func.max(x_axis)).scalar()
    n = db.query(x_axis).count()

    distance = Xmax - Xmin

    #Number of gaps
    #k = math.ceil(1.33 * math.log(n,10))
    k = math.ceil(math.sqrt(n))

    #Gap size
    h = math.ceil(distance/k)

    response = {
        'label': [],
        'amount': []
    }

    val = Xmin

    while val <= Xmax:
        val += h
        response['label'].append(str(val-h) + ' - ' + str(val))
        amount = round(db.query(func.avg(y_axis)).filter(keystroke.user_id == survey.id).filter(x_axis.between(val-h,val)).first()[0],1)
        response['amount'].append(amount)
        val += 1

    return response

def age_vs_enc(db: Session):

    return vs_plot(models.survey.age, models.keystroke_statistic.enc, db)

def age_vs_asit(db: Session):

    return vs_plot(models.survey.age, models.keystroke_statistic.asit, db)

def rollover_vs_asit(db: Session):

    return vs_plot(models.keystroke_statistic.rollover, models.keystroke_statistic.asit, db)

def rollover_vs_atst(db: Session):

    return vs_plot(models.keystroke_statistic.rollover, models.keystroke_statistic.atst, db)

def lang_enc(db: Session):

    survey = models.survey
    keystroke = models.keystroke_statistic

    polish = db.query(func.avg(keystroke.enc)).filter(keystroke.user_id == survey.id).filter(survey.isPolishNative == m_isPolishNative['yes']).first()

    not_polish = db.query(func.avg(keystroke.enc)).filter(keystroke.user_id == survey.id).filter(survey.isPolishNative == m_isPolishNative['no']).first()

    return{
        'polish': round(polish[0], 1),
        'not_polish': round(not_polish[0], 1)
    }

def lang_ec(db: Session):

    survey = models.survey
    keystroke = models.keystroke_statistic

    polish = db.query(func.avg(keystroke.ec)).filter(keystroke.user_id == survey.id).filter(survey.isPolishNative == m_isPolishNative['yes']).first()

    not_polish = db.query(func.avg(keystroke.ec)).filter(keystroke.user_id == survey.id).filter(survey.isPolishNative == m_isPolishNative['no']).first()

    return{
        'polish': round(polish[0], 1),
        'not_polish': round(not_polish[0], 1)
    }

def so_sa_sch(db: Session):

    sa = db.query(func.sum(models.keystroke_statistic.sa)).first()[0]

    so = db.query(func.sum(models.keystroke_statistic.so)).first()[0]

    sch = db.query(func.sum(models.keystroke_statistic.sch)).first()[0]

    total = sa + so + sch

    sa_ratio = round(sa/total, 1)
    sch_ratio = round(sch/total, 1)

    return{
        'sa': sa_ratio,
        'so': 1 - sa_ratio - sch_ratio,
        'sch': sch_ratio
    }

def long_lostalt_invalidcase_other(db: Session):

    lostAlt = db.query(func.sum(models.keystroke_statistic.lostAlt)).first()[0]

    longAlt = db.query(func.sum(models.keystroke_statistic.longAlt)).first()[0]

    invalidCase = db.query(func.sum(models.keystroke_statistic.invalidCase)).first()[0]

    sch = db.query(func.sum(models.keystroke_statistic.sch)).first()[0]

    lostAlt_ratio = round(lostAlt/sch, 1)
    longAlt_ratio = round(longAlt/sch, 1)
    invalidCase_ratio = round(invalidCase/sch, 1)

    return {
        'lostAlt': lostAlt_ratio,
        'longAlt': longAlt_ratio,
        'invalidCase': invalidCase_ratio,
        'other': 1 - lostAlt_ratio - longAlt_ratio - invalidCase_ratio
    }

def education_vs_asit(db: Session):

    survey = models.survey
    keystroke = models.keystroke_statistic

    primary = db.query(func.avg(keystroke.asit)).filter(keystroke.user_id == survey.id).filter(survey.education == m_education['primary']).first()

    high = db.query(func.avg(keystroke.asit)).filter(keystroke.user_id == survey.id).filter(survey.education == m_education['high']).first()

    student = db.query(func.avg(keystroke.asit)).filter(keystroke.user_id == survey.id).filter(survey.education == m_education['student']).first()

    graduate = db.query(func.avg(keystroke.asit)).filter(keystroke.user_id == survey.id).filter(survey.education == m_education['graduate']).first()

    undergraduate = db.query(func.avg(keystroke.asit)).filter(keystroke.user_id == survey.id).filter(survey.education == m_education['undergraduate']).first()

    return {
        'primary': primary[0],
        'high': high[0],
        'student': student[0],
        'graduate': graduate[0],
        'undergraduate': undergraduate[0]
    }