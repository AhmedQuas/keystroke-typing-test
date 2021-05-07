from .. import schemas

def total_chars(request: schemas.keystroke):
    """
        Returun total number of chars in given reguest
    """
    total_chars_number = 0

    for sentence in range(len(request)):
        total_chars_number += len(request[sentence])

    return total_chars_number
