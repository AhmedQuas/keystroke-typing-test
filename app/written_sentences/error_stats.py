from .. import schemas
from typing import List
import Levenshtein

def error_statistics(correct_sentences: List[str], written_sentences: List[str], keystroke_stats: schemas.keystroke_stats):
    """
        Use Levenshtein.editops to get types of mistakes and calculate number of specific mistakes
    """
    #Levenshtein leditops loop

    for sentence in range(len(correct_sentences)):
            for word in range(len(correct_sentences[sentence])):
                differences = Levenshtein.editops(correct_sentences[sentence][word], written_sentences[sentence][word])
                #Uncomment to show differences that has been found
                #print(differences)

                if len(differences):
                    for difference in differences:
                        diff_type = difference[0]

                        if diff_type is 'delete':
                            keystroke_stats.so += 1
                        elif diff_type is 'insert':
                            keystroke_stats.sa += 1
                        else:
                            keystroke_stats.sch += 1
                            correct_index = difference[1]
                            written_index = difference[2]
                            correct_word = correct_sentences[sentence][word]
                            written_word = written_sentences[sentence][word]
                            sch(correct_index, written_index ,correct_word, written_word, keystroke_stats)

    keystroke_stats.enc = keystroke_stats.sa + keystroke_stats.so + keystroke_stats.sch

def sch(correct_index: int, written_index: int, correct_word: str, written_word: str, keystroke_stats: schemas.keystroke_stats):

    correct_char = correct_word[correct_index]
    written_char = written_word[written_index]
    
    alt_mistake(correct_char, written_char, keystroke_stats)
    invalidCase(correct_char, written_char, keystroke_stats)

def alt_mistake(c1: str, c2: str, keystroke_stats: schemas.keystroke_stats):
    """
        Find lostAlt and longAlt mistakes
    """

    #Polish diactric marks
    pl_diactric_marks = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
    no_alt_diat_marks = ['a', 'c', 'e', 'l', 'n', 'o', 's', 'x', 'z']

    if c1 in pl_diactric_marks:
        index =pl_diactric_marks.index(c1)
        if c2 == no_alt_diat_marks[index]:
            #lostAlt
            keystroke_stats.lostAlt += 1

    if c1 in no_alt_diat_marks:
        index =no_alt_diat_marks.index(c1)
        if c2 == pl_diactric_marks[index]:
            #longAlt
            keystroke_stats.longAlt += 1

def invalidCase(c1: str, c2: str, keystroke_stats: schemas.keystroke_stats):
    """
        Detect invalid case mistake
    """

    if c1.upper() == c2.upper():
        keystroke_stats.invalidCase += 1