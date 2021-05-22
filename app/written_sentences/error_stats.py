from .. import schemas
from typing import List
import Levenshtein

def error_statistics(correct_sentences: List[str], written_sentences: List[str], keystroke_stats: schemas.keystroke_stats):
    """
        Use Levenshtein.editops to get types of mistakes and calculate number of specific mistakes
    """
    #lenvenstin loop

    for sentence in range(len(correct_sentences)):
            for word in range(len(correct_sentences[sentence])):
                differences = Levenshtein.editops(correct_sentences[sentence][word], written_sentences[sentence][word])
                print(differences)

                if len(differences):
                    for difference in differences:
                        diff_type = difference[0]

                        if diff_type is 'delete':
                            keystroke_stats.so += 1
                        elif diff_type is 'insert':
                            keystroke_stats.sa += 1
                        else:
                            correct_index = difference[1]
                            written_index = difference[2]
                            correct_word = correct_sentences[sentence][word]
                            written_word = written_sentences[sentence][word]
                            sch(correct_index, written_index ,correct_word, written_word)
    
    return 0

def sch(correct_index: int, written_index: int, correct_word: str, written_word: str):

    correct_char = correct_word[correct_index]
    written_char = written_word[written_index]
    
    longAlt(correct_char, written_char)
    lostAlt(correct_char, written_char)
    invalidCase(correct_char, written_char)

def longAlt(c1: str, c2: str):
    pass

def lostAlt(c1: str, c2: str):
    pass

def invalidCase(c1: str, c2: str):
    pass