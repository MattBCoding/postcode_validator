import re


class Rules:
    """
    Validation regex rules for postcode(s)
    source(s):
    https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Validation
    """

    UK = (
        "^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?"
        "[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?"
        "[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"
    )
