import json, requests
from typing import List


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

def get_test_sentence():
    """
        Make API request to /sentences to get correct words
    """
    
    response = requests.get('http://127.0.0.1/sentences')
    json_data = json.loads(response.text)

    written_sentences_dict = json_data['sentences']
    
    written_sentences = sentences_word_split(written_sentences_dict)

    return written_sentences
