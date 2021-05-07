from . import schemas

def keystroke_statistics(request: schemas.keystroke, keystrokes: schemas.keystroke_fingerprint):
    """
        Register statistics functions below
    """

    rollover(request, keystrokes)
    print('Inside register function', keystrokes.rollover)

def rollover(request: schemas.keystroke, keystrokes: schemas.keystroke_fingerprint):

    prev_keystroke_upTimeStamp = 0

    for sentence in range(len(request)):
        for char in range(len(request[sentence])):

            if (request[sentence][char].downTimeStamp < prev_keystroke_upTimeStamp):
                keystrokes.rollover +=1
                #print(request[sentence][char]) #Uncomment to see rollover keys in fastapi console
            prev_keystroke_upTimeStamp = request[sentence][char].upTimeStamp
