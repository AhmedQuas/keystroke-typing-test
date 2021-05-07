from sqlalchemy.orm import Session
from typing import List
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

def add_test_data(request: List[List[schemas.keystroke]], db: Session):
    """
        App logic for /test-data endpoint
    """
    #print(request[0][0].key)
    validators.validate_data(request)

    keystroke_stats = schemas.keystroke_stats()
    keystroke_statistics.keystroke_statistics(request, keystroke_stats)

    print('final keystroke', keystroke_stats)
