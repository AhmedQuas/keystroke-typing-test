from fastapi import HTTPException, status
from .. import schemas
from typing import List
from . import helpers
# For json debug purpose only pprint.pprint(request)
import pprint, json
import Levenshtein


def validate_written_sentence_data(written_sentence: List[str], keystrokes: List[schemas.keystroke]):
    """
        Register sanitize function & validation checks inside this function
    """
    written_sentences_split = helpers.sentences_word_split(written_sentence)
    correct_sentences_split = helpers.get_test_sentence()

    prefiltered_data = calc_levenshtein(written_sentences_split, correct_sentences_split, keystrokes)

    #print('written_sentence =>', prefiltered_data['written_sentences'])
    #print('correct_sentence =>', prefiltered_data['correct_sentences'])

    return prefiltered_data

####################################
# Validation checks implementation #
####################################

def calc_levenshtein(written_sentence: List[str], correct_sentence: List[str], keystrokes: List[schemas.keystroke]):
    """
        Calc levenshtein metric and remove sentences that have word with metric bigger than 4. 
        Alo throw exception in case the number of words do not match between interviewee and correct sentences
    """
    
    if len(correct_sentence) != len(written_sentence):
        raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail ={'msg':'Given data set fail during validation:calc_levenshtein_1'})
    
    #Remove sentence that have different number of words
    removed_obj = True

    while removed_obj:
        removed_obj = False
        for sentence in range(len(correct_sentence)):
            if len(correct_sentence[sentence]) != len(written_sentence[sentence]):
                helpers.remove_sentence(sentence, written_sentence, correct_sentence, keystrokes)
                removed_obj = True
                break

    #print('correct', correct_sentence)
    #print('wiritten', written_sentence)

    #Array used to make sure that we remove all unnecessary keys which have Levenshtein distance more than 3
    removed_obj = True

    while removed_obj:
        removed_obj = False
        for sentence in range(len(correct_sentence)):
            for word in range(len(correct_sentence[sentence])):
                if Levenshtein.distance(written_sentence[sentence][word],correct_sentence[sentence][word]) > 3:
                    helpers.remove_sentence(sentence, written_sentence, correct_sentence, keystrokes)
                    removed_obj = True
                    break
            if removed_obj == True:
                break

    return {
        'written_sentences': written_sentence,
        'correct_sentences': correct_sentence,
        'keystrokes': keystrokes
    }
