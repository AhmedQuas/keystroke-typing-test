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