from fastapi import HTTPException, status
from .. import schemas
from typing import List
from . import helpers
# For json debug purpose only pprint.pprint(request)
import pprint, json


def validate_written_sentence_data(written_sentence: List[str]):
    """
        Register sanitize function & validation checks inside this function
    """
    written_sentences_split = helpers.sentences_word_split(written_sentence)
    correct_sentences_split = helpers.get_test_sentence()


    #print('leavenstain',written_sentences_split)

def calc_levenshtein():
    pass