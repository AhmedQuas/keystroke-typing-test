from enum import Enum

# Database enum mapper
# Following best practises it should be done using relationships in db
# But due to increase speed of operations it is done by enum mapper


isPolishNative = {
    'no': 0,
    'yes': 1
}

handPreference = {
    'left': 0,
    'right': 1
}

sex = {
    'woman': 0,
    'man': 1
}

education = {
    'primary': 0,
    'high': 1,
    'student': 2,
    'graduate': 3,
    'undergraduate': 4
}

employment = {
    'unemployed' : 0,
    'withcomputer' : 1,
    'withoutcomputer' : 2
}

likeScience = {
    'yes' : 1,
    'no' : 0
}
