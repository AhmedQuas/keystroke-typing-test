from . import schemas
from .helpers import statistics

def keystroke_statistics(request: schemas.keystroke, keystroke_stat: schemas.keystroke_stats):
    """
        Register statistics functions below
    """

    keystroke_stat.rollover = rollover(request)
    keystroke_stat.asit = asit(request)
    keystroke_stat.aspt = aspt(request)
    keystroke_stat.atst = atst(request)
    keystroke_stat.att = att(request)
    keystroke_stat.ec = ec(request)
    keystroke_stat.tfs = tfs(request)

def rollover(request: schemas.keystroke):
    """
        Count occurances of rollover
    """
    prev_keystroke_upTimeStamp = 0
    rollover = 0

    for sentence in range(len(request)):
        for char in range(len(request[sentence])):

            if (request[sentence][char].downTimeStamp < prev_keystroke_upTimeStamp):
                rollover +=1
                #print(request[sentence][char]) #Uncomment to see rollover keys in fastapi console
            prev_keystroke_upTimeStamp = request[sentence][char].upTimeStamp

    return rollover

def asit(request: schemas.keystroke):
    """
        Count Average Sign Time
    """

    total_chars_number = statistics.total_chars(request)

    total_chars_press_time = 0

    for sentence in request:
        for keystroke in sentence:
            total_chars_press_time += keystroke.upTimeStamp - keystroke.downTimeStamp

    return total_chars_press_time/total_chars_number

def aspt(request: schemas.keystroke):
    """
        Count Average Space Time
    """

    space_count = 0
    total_space_time = 0

    prev_keystroke = request[0][0]

    for sentence in range(len(request)):
        for char in range(len(request[sentence])):

            if (request[sentence][char].key is ' '):
                space_count +=1
                
                #Array overflow
                if len(request[sentence]) is (char + 1):
                    total_space_time += request[sentence][char].upTimeStamp - prev_keystroke.upTimeStamp
                else:
                    total_space_time += request[sentence][char+1].downTimeStamp - prev_keystroke.upTimeStamp

            prev_keystroke = request[sentence][char]

    return total_space_time/space_count

def atst(request: schemas.keystroke):
    """
        Count Average Tap Space Time
    """

    total_chars_number = statistics.total_chars(request)
    total_tap_space_time = 0

    prev_keystroke = request[0][0]

    for sentence in range(len(request)):
        for char in range(len(request[sentence])):
            if not(sentence is 0 and char is 0) and (request[sentence][char].downTimeStamp > prev_keystroke.upTimeStamp):
                    total_tap_space_time += request[sentence][char].downTimeStamp - prev_keystroke.upTimeStamp
            #else:  #Uncomment to see exclude keystrokes
            #    print('request[',sentence,',',char,']')

            prev_keystroke = request[sentence][char]

    return total_tap_space_time/total_chars_number

def att(request: schemas.keystroke):
    """
        Count Average Tap Time
    """

    total_chars_number = statistics.total_chars(request)

    for sentence in request:
        for keystroke in sentence:
            total_tap_time = keystroke.upTimeStamp - keystroke.downTimeStamp

    return total_tap_time/total_chars_number

def ec(request: schemas.keystroke):
    """
        Count number of backspace & delete chars
    """

    total_backspaces = 0
    char_remove_keys = ['Backspace', 'Delete']
    
    for sentence in request:
        for keystroke in sentence:
            if(keystroke.key in char_remove_keys):
                total_backspaces += 1

    return total_backspaces

def tfs(request: schemas.keystroke):
    """
        Count Taps for Sign - number of keystroke.repeat occurences
    """
    
    repeated_chars = 0

    for sentence in request:
        for keystroke in sentence:
            if(keystroke.repeat is True):
                repeated_chars += 1

    return repeated_chars