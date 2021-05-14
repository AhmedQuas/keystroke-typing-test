from sqlalchemy.orm import Session
from typing import List, Dict
from . import schemas, models, validators, keystroke_erros, keystroke_statistics
from .validators import validate_data

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

    validators.validate_data(keystrokes)

    keystroke_stats = schemas.keystroke_stats()
    keystroke_statistics.keystroke_statistics(keystrokes, keystroke_stats)

    print(keystroke_stats)
