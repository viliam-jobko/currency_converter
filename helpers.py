# coding=utf-8

def symbolToLetters(symbol):
    symbolsToLetters = {
        'лв':   'BGN',
        'R$':   'RBL',
        '¥':    'CNY',
        '£':    'GBP',
        '₪':    'ILS',
        '₩':    'KRW',
        '₱':    'PHP',
        '฿':    'THB',
        '$':    'USD',
    }

    try:
        symbolsToLetters[symbol]
    except NameError:
        return False
    else:
        return symbolsToLetters[symbol]

