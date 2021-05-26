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
