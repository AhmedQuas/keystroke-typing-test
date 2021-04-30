from fastapi import HTTPException, status
from . import schemas
# For json debug purpose only
import pprint

def validate_data(request: schemas.survey):
    """
        Register sanitize function & validation checks inside this function
    """
    
    #Sanitization functions
    assing_true_key_up_value(request)
    
    #Validation checks
    negative_check(request)

#########################################
# Sanitiazion functions implementations #
#########################################

def assing_true_key_up_value(request: schemas.survey):
    """
        Assign true upTimeStamp for Alt or Shift key combinations
    """

    shortcut_keys = ['Shift', 'AltGraph']

    for sentence in range(len(request)):
        for char in range(len(request[sentence])):

            keystroke = request[sentence][char]
            
            if (keystroke.key in shortcut_keys):
                request[sentence][char+1].upTimeStamp = keystroke.upTimeStamp

####################################
# Validation checks implementation #
####################################

def negative_check(request: schemas.survey):
    """
        Check if downTimeStamp or upTimeStamp is negative value
    """

    for sentence in range(len(request)):
        for char in range(len(request[sentence])):

            keystroke = request[sentence][char]
            
            if (keystroke.downTimeStamp < 0 or keystroke.upTimeStamp < 0):
                raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                detail = 'Given data set fail during validation stage')

    pprint.pprint(request)
