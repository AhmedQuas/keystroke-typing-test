from .. import schemas
from typing import List, Dict
# For json debug purpose only pprint.pprint(request)
import pprint, json

def data_deserialize(request: List[Dict]):
    """
        Function is used to deserialize JSON that come from interviewee
    """

    #Deserialization of survey data
    survey_dict = request[0]['survey']
    survey_object = schemas.survey(**survey_dict)
    #print('survey_object', ' = ', type(survey_object))
    
    #Deserialization of keystroke
    keystrokes_dict = request[0]['keystrokes']

    keystrokes = []
    i = 0

    for sentence in keystrokes_dict:
        keystrokes.append([])
        for keystroke in sentence:
            keystroke_object = schemas.keystroke(**keystroke)
            keystrokes[i].append(keystroke_object)
        i += 1
    
    #print(type(keystrokes[0][0]))

    #Deserialization of written sentences
    written_sentences_dict = request[0]['written-sentences']

    additional_sentence_queue = request[0]['additionalSentenceQueue']

    #print(additional_sentence_queue)

    return {
        'survey': survey_object,
        'keystrokes': keystrokes,
        'written_sentences': written_sentences_dict,
        'additional_sentence_queue': additional_sentence_queue
    }
    