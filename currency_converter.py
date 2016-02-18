#!/usr/bin/python
# coding=utf-8
import argparse
from helpers import *

parser = argparse.ArgumentParser(description='This is a converter for currencies. For available currencies check http://api.fixer.io/latest')
parser.add_argument('--amount', help='Amount which you want to convert', required=True, type=float)
parser.add_argument('--input_currency', help='Input currency: 3 letters name or currency symbol, e.g. USD, EUR, $, €', required=True)
parser.add_argument('--output_currency', help='Requested currency: same format as Input currency. Omit to convert to all known currencies', required=False)
args = parser.parse_args()

amount = args.amount
input_currency = args.input_currency
output_currency = args.output_currency

#convert currency symbols
if symbolToLetters(input_currency):
    input_currency = symbolToLetters(input_currency)
if symbolToLetters(output_currency):
    output_currency = symbolToLetters(output_currency)

#get exchange rate
exchangeRates = getExchangeRates(input_currency, output_currency)