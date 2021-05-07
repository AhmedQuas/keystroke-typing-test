from fastapi import HTTPException, status
from . import schemas
# For json debug purpose only pprint.pprint(request)
import pprint, json

def validate_data(request: schemas.keystroke):
    """
        Register sanitize function & validation checks inside this function
    """
    
    #Sanitization functions
    assing_true_key_up_value(request)
    remove_unnecessary_keys(request)
    
    #Validation checks
    negative_check(request)
    key_up_before_key_down_check(request)
    key_press_chronological_check(request)
    invalid_key_value_check(request)

    #last_check(request)

#########################################
# Sanitiazion functions implementations #
#########################################

def assing_true_key_up_value(request: schemas.keystroke):
    """
        Assign true upTimeStamp for Alt or Shift key combinations
    """

    shortcut_keys = ['Shift', 'AltGraph']

    for sentence in range(len(request)):
        for char in range(len(request[sentence])):

            keystroke = request[sentence][char]
            
            if (keystroke.key in shortcut_keys and request[sentence][char+1].upTimeStamp is 0):
                request[sentence][char+1].upTimeStamp = keystroke.upTimeStamp

            if (keystroke.key not in shortcut_keys and request[sentence][char].upTimeStamp is 0):
                request[sentence][char].upTimeStamp = keystroke.downTimeStamp

def remove_unnecessary_keys(request: schemas.keystroke):
    """
        Remove keys not used in further calcucations e.x Shift or Alt Combinations
    """

    necessary_keys = ['Backspace','Delete']
    removed_obj = True

    #Array used to make sure that we remove all unnecessary keys
    while removed_obj:
        removed_obj = False
        for sentence in range(len(request)):
                for keystroke in request[sentence]:
                    if not (len(keystroke.key) is 1 or keystroke.key in necessary_keys):
                        removed_obj = True
                        request[sentence].remove(keystroke)

"""
    for sentence in range(len(request)):
            for keystroke in request[sentence]:
                if not (len(keystroke.key) is 1 or keystroke.key in necessary_keys):
                    request[sentence].remove(keystroke)
"""

####################################
# Validation checks implementation #
####################################

def negative_check(request: schemas.keystroke):
    """
        Check if downTimeStamp or upTimeStamp is negative value
    """

    for sentence in range(len(request)):
        for char in range(len(request[sentence])):

            keystroke = request[sentence][char]
            
            if (keystroke.downTimeStamp < 0 or keystroke.upTimeStamp < 0):
                raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail ={'msg':'Given data set fail during validation:negative_check stage'})

def key_up_before_key_down_check(request: schemas.keystroke):
    """
        Check if key press was before key up
    """

    for sentence in request:
        for keystroke in sentence:
            if(keystroke.downTimeStamp > keystroke.upTimeStamp ):
                raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail ={'msg':'Given data set fail during validation:key_up_before_key_down_check stage'})

def key_press_chronological_check(request: schemas.keystroke):
    """
        Check if downTimeStamp is chronological value
    """

    prev_keystroke_downTimeStamp = 0

    for sentence in range(len(request)):
        for char in range(len(request[sentence])):
            
            current_keystroke_downTimeStamp = request[sentence][char].downTimeStamp

            if (current_keystroke_downTimeStamp < prev_keystroke_downTimeStamp):
                raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail ={'msg':'Given data set fail during validation:key_press_chronological_check stage'})
            prev_keystroke_downTimeStamp = current_keystroke_downTimeStamp

def invalid_key_value_check(request: schemas.keystroke):
    """
        Check if key field contains invalid value - multicharacter value not specified in valid_multi_char_keys list
    """
    
    valid_multi_char_keys = ['Backspace','Delete']

    for sentence in request:
        for keystroke in sentence:
            if not(len(keystroke.key) is 1 or keystroke.key in valid_multi_char_keys):
                raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail ={'msg':'Given data set fail during validation:invalid_key_value_check stage'})

def last_check(request: schemas.keystroke):
    """
        Last check used for checking the pipeline output => debug & testing purpose only
    """
    pprint.pprint(request)
    """
    raise HTTPException(status_code = status.HTTP_200_OK,
                detail ={'msg':'All ok it it only dump of final pipeline',
                'pipeline_output':json_convert(request)})
    """

#################
# Debug helpers #
#################

def json_convert(request: schemas.keystroke):
    """
        # For json debug purpose only pprint.pprint(request)
    """
    json_data = ""

    for sentence in request:
        for keystroke in sentence:
            json_data += keystroke.toJSON()
    
    return json_data
    #raise http exception'request':json_convert(request)})
    #print('INVALID VALUE NEAR',keystroke)
