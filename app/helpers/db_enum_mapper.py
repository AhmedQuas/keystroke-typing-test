from enum import Enum

# Database enum mapper
# Following best practises it should be done using relationships in db
# But due to increase speed of operations it is done by enum mapper

class isPolishNative(Enum):
    YES = 1
    NO = 0

class sex(Enum):
    WOMAN = 0
    MAN = 1

class handPreference(Enum):
    LEFT = 0
    RIGHT = 1

class education(Enum):
    PRIMARY = 0
    HIGH = 1
    STUDENT = 2
    GRADUATE = 3
    UNDERGRADUATE = 4

class employment(Enum):
    UNEMPLOYEMNT = 0
    WITHCOMPOUTER = 1
    WITHOUTCOMPUTER = 2

class likeScience(Enum):
    YES = 1
    NO = 0