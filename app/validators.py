from fastapi import HTTPException, status
from . import schemas
# For json debug purpose only pprint.pprint(request)
import pprint

def validate_data(request: schemas.test_data):
    """
        Register sanitize function & validation checks inside this function
    """
    
    #Sanitization functions
    assing_true_key_up_value(request)
    remove_unnecessary_keys(request)
    
    #Validation checks
    negative_check(request)
    key_up_before_key_down_check(request)

    last_check(request)

#########################################
# Sanitiazion functions implementations #
#########################################

def assing_true_key_up_value(request: schemas.test_data):
    """
        Assign true upTimeStamp for Alt or Shift key combinations
    """

    shortcut_keys = ['Shift', 'AltGraph']

    for sentence in range(len(request)):
        for char in range(len(request[sentence])):

            keystroke = request[sentence][char]
            
            if (keystroke.key in shortcut_keys):
                request[sentence][char+1].upTimeStamp = keystroke.upTimeStamp

def remove_unnecessary_keys(request: schemas.test_data):
    """
        Remove keys not used in further calcucations e.x Shift or Alt Combinations
    """

    unnecessary_keys = ['Shift', 'AltGraph']

    for sentence in range(len(request)):
        for keystroke in request[sentence]:
            if(keystroke.key in unnecessary_keys ):
                request[sentence].remove(keystroke)

####################################
# Validation checks implementation #
####################################

def negative_check(request: schemas.test_data):
    """
        Check if downTimeStamp or upTimeStamp is negative value
    """

    for sentence in range(len(request)):
        for char in range(len(request[sentence])):

            keystroke = request[sentence][char]
            
            if (keystroke.downTimeStamp < 0 or keystroke.upTimeStamp < 0):
                raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                detail = 'Given data set fail during validation:negative_check stage')

def key_up_before_key_down_check(request: schemas.test_data):
    """
        Check if downTimeStamp or upTimeStamp is negative value
    """

    for sentence in request:
        for keystroke in sentence:
            if(keystroke.downTimeStamp > keystroke.upTimeStamp ):
                raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                detail = 'Given data set fail during validation:key_up_before_key_down_check stage')
                

def last_check(request: schemas.survey):
    """
        Last check used for checking the pipeline output => debug & testing purpose only
    """
    #pprint.pprint(request)
