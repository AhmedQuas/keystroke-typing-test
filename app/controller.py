from sqlalchemy.orm import Session
from typing import List, Dict
from . import schemas, models, keystroke_erros
from .keystroke.validators import validate_keystroke_data
from .keystroke.statistics import keystroke_statistics
from .written_sentences.validators import validate_written_sentence_data
from .written_sentences.error_stats import error_statistics

def add_survey(request: schemas.survey, db: Session):
    """
        App logic for /survey endpoint
    """
    new_survey_entry = models.survey(
        age = request.age, 
        isPolishNative = request.isPolishNative,
        sex = request.sex,
        handPreference = request.handPreference,
        education = request.education,
        employment = request.employment,
        likeScience = request.likeScience)
    
    db.add(new_survey_entry)
    db.commit()
    
    #print(request.q1)
    return new_survey_entry

def add_data(data: List[Dict], db: Session):
    """
        App logic for /test-data endpoint
    """

    survey = data['survey']
    keystrokes = data['keystrokes']
    written_sentences = data['written_sentences']
    additional_sentence_queue = data['additional_sentence_queue']

    # Return all 10 sentences that will be processed
    data=validate_written_sentence_data(written_sentences, keystrokes, additional_sentence_queue)
    
    keystrokes = data['keystrokes']
    correct_sentences = data['correct_sentences']
    written_sentences = data['written_sentences']

    validate_keystroke_data(keystrokes)

    keystroke_stats = schemas.keystroke_stats()

    error_statistics(correct_sentences, written_sentences, keystroke_stats)

    keystroke_statistics(keystrokes, keystroke_stats)

    #print(keystroke_stats)

    add_survey(survey, db)
    
    query = db.query(models.survey).order_by(models.survey.id.desc())

    user = query.first()

    new_keystroke_statistics = models.keystroke_statistic(
        user_id = user.id,
        rollover = keystroke_stats.rollover,
        asit = keystroke_stats.asit,
        aspt = keystroke_stats.aspt,
        atst = keystroke_stats.atst,
        att = keystroke_stats.att,
        ec = keystroke_stats.ec,
        enc = keystroke_stats.enc,
        tfs = keystroke_stats.tfs,
        sch = keystroke_stats.sch,
        so = keystroke_stats.so,
        sa = keystroke_stats.sa,
        longAlt = keystroke_stats.longAlt,
        lostAlt = keystroke_stats.lostAlt,
        invalidCase = keystroke_stats.invalidCase,
        capsLockUsage =  keystroke_stats.capsLockUsage
    )

    db.add(new_keystroke_statistics)
    db.commit()
