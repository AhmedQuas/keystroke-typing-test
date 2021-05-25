import json, requests
from typing import List
from .. import schemas


def sentences_word_split(sentences: List[str]):
    """
        Split given list of sentences into words
    """
    result = []
    sentence_str = ''

    for sentence in sentences:
        result.append(sentence.split())

    #Array used to make sure that we remove all unnecessary keys
    removed_obj = True
    
    while removed_obj:
        removed_obj = False
        for sentence in range(len(result)):
            for word in range(len(result[sentence])):
                if result[sentence][word] == ' ':
                    removed_obj = True
                    result[sentence].remove(word)

    return result

def get_test_sentence(additional_sentence_queue: List[int]):
    """
        Make API request to /sentences to get correct words
    """
    
    response = requests.get('http://127.0.0.1/sentences')
    json_data = json.loads(response.text)

    written_sentences_dict = json_data['sentences']

    for index in additional_sentence_queue:
        written_sentences_dict.append(written_sentences_dict[index])
    
    written_sentences = sentences_word_split(written_sentences_dict)
    #print('api:',written_sentences)
    return written_sentences

def remove_sentence(index:int, written_sentence: List[str], correct_sentence: List[str], keystrokes: List[schemas.keystroke]):
    """
        Delete all data that is related with sentence that will be removed
    """

    del written_sentence[index]
    del correct_sentence[index]
    
    #keystroke remove loop
    #check if it is first sentence or last sentence
    if (index is 0) or (index is len(keystrokes)-1):
        del keystrokes[index]

    else:
        last_correct_sentence = keystrokes[index - 1]
        last_correct_keystroke = last_correct_sentence[len(last_correct_sentence)-1]
        #calculate difference
        diff = keystrokes[index+1][0].downTimeStamp - last_correct_keystroke.upTimeStamp
        
        del keystrokes[index]

        #substract the difference for each next keystroke
        for sentence in range(index, len(keystrokes)-1):
            for keystroke in keystrokes[index]:
                keystroke.downTimeStamp -= diff
                keystroke.upTimeStamp -= diff

    return {
        'written_sentence': written_sentence,
        'correct_sentence': correct_sentence,
        'keystrokes': keystrokes
    }