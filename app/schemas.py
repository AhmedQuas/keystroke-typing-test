from pydantic import BaseModel
import json

class keystroke(BaseModel):
    key: str
    downTimeStamp: int
    upTimeStamp: int
    repeat: bool
    shiftKey: bool

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=0)

class survey(BaseModel):
    age: int
    isPolishNative: bool
    sex: bool
    handPreference: bool
    education: int
    employment: int
    likeScience: bool

class keystroke_stats(BaseModel):
    rollover = 0
    asit = 0        #Average Sign Time
    aspt = 0        #Average Space Time
    atst = 0        #Average Tap Space Time
    att = 0         #Average Tap Time
    ec = 0          #Errors Corrected
    enc = 0         #Errors Not Corrected
    tfs = 0         #Taps for sign
    sch = 0         #Sign change
    so = 0          #Sign ommission
    sa = 0          #Sign addtion
    longAlt = 0
    lostAlt = 0
    invalidCase = 0
    capsLockUsage = False
