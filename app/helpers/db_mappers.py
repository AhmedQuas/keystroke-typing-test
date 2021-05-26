# Database mappers
# Following best practises it should be done using relationships in db
# But due to increase speed of operations it is done by mapper


m_isPolishNative = {
    'no': 0,
    'yes': 1
}

m_handPreference = {
    'left': 0,
    'right': 1
}

m_sex = {
    'woman': 0,
    'man': 1
}

m_education = {
    'primary': 0,
    'high': 1,
    'student': 2,
    'graduate': 3,
    'undergraduate': 4
}

m_employment = {
    'unemployed' : 0,
    'withcomputer' : 1,
    'withoutcomputer' : 2
}

m_likeScience = {
    'yes' : 1,
    'no' : 0
}
