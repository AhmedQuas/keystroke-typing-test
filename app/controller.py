from sqlalchemy.orm import Session
from typing import List
from . import schemas, models
from .validators import validate_data

def add_survey(request: schemas.survey, db: Session):
    """
        App logic for /survey endpoint
    """
    new_survey_entry = models.survey(q1 = request.q1, q2 = request.q2)
    
    db.add(new_survey_entry)
    db.commit()
    
    #print(request.q1)
    return new_survey_entry

def add_test_data(request: List[List[schemas.test_data]]):
    """
        App logic for /test-data endpoint
    """
    #print(request[0][0].key)
    validate_data(request)
