from typing import List
from . import schemas

def add_survey(request: schemas.survey):
    """
        App logic for /survey endpoint
    """
    #print(request.q1)
    pass

def add_test_data(request: List[List[schemas.test_data]]):
    """
        App logic for /test-data endpoint
    """
    #print(request[0][0].key)
    pass
