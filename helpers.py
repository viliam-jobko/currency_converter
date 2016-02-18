# coding=utf-8
import urllib2, json

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

    if symbol in symbolsToLetters:
        return symbolsToLetters[symbol]
    else:
        return False



def apiBuildUrl(base, symbol):
    baseUrl = 'http://api.fixer.io/latest'

    url = baseUrl + '?base=' + base

    if symbol:
        url += '&symbols=' + symbol

    return url



def getExchangeRates(base, symbol):
    url = apiBuildUrl(base, symbol)

    try:
        response = urllib2.urlopen(url)
        exchangeRatesJSON = response.read()
    except urllib2.HTTPError, e:
        print 'Cannot download Exchange reates.',
        print 'HTTP Error code:', e.code
        return False
    except urllib2.URLError, e:
        print 'Cannot download Exchange reates.',
        print 'Reason:', e.reason
        return False
    else:
        exchangeRates = json.loads(exchangeRatesJSON)
        if 'error' in exchangeRates:
            print 'There is error in your input:', exchangeRates['error']
            return False
        if exchangeRates['rates'] == {}:
            print 'Unknown output currency.'
            return False

    return exchangeRates

