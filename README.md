# currency_converter
Entry task to PythonMaster. This is my first Python script ever (not counting Codecademy curses).

##Usage

```
./currency_converter.py -h
usage: currency_converter.py [-h] --amount AMOUNT --input_currency
                             INPUT_CURRENCY
                             [--output_currency OUTPUT_CURRENCY]

This is a converter for currencies. For available currencies check
http://api.fixer.io/latest

optional arguments:
  -h, --help            show this help message and exit
  --amount AMOUNT       Amount which you want to convert
  --input_currency INPUT_CURRENCY
                        Input currency: 3 letters name or currency symbol,
                        e.g. USD, EUR, $, €
  --output_currency OUTPUT_CURRENCY
                        Requested currency: same format as Input currency.
                        Omit to convert to all known currencies
```

```
./currency_converter.py --amount 100.0 --input_currency EUR --output_currency CZK
{
    "input": {
        "amount": 100.0, 
        "currency": "EUR"
    }, 
    "output": {
        "CZK": 2703.0
    }
}
```

```
./currency_converter.py --amount 0.9 --input_currency ¥ --output_currency AUD
{
    "input": {
        "amount": 0.9, 
        "currency": "CNY"
    }, 
    "output": {
        "AUD": 0.19
    }
}
```

```
./currency_converter.py --amount 10.92 --input_currency £
{
    "input": {
        "amount": 10.92, 
        "currency": "GBP"
    }, 
    "output": {
        "AUD": 21.94, 
        "BGN": 27.69, 
        "BRL": 63.03, 
        "CAD": 21.47, 
        "CHF": 15.61, 
        "CNY": 102.26, 
        "CZK": 382.63, 
        "DKK": 105.65, 
        "EUR": 14.16, 
        "HKD": 122.05, 
        "HRK": 107.83, 
        "HUF": 4380.99, 
        "IDR": 211640.52, 
        "ILS": 61.3, 
        "INR": 1075.05, 
        "JPY": 1785.97, 
        "KRW": 19282.54, 
        "MXN": 286.09, 
        "MYR": 65.45, 
        "NOK": 134.81, 
        "NZD": 23.68, 
        "PHP": 745.92, 
        "PLN": 62.03, 
        "RON": 63.15, 
        "RUB": 1181.65, 
        "SEK": 133.08, 
        "SGD": 22.03, 
        "THB": 558.03, 
        "TRY": 46.55, 
        "USD": 15.69, 
        "ZAR": 241.57
    }
}
```

##Known issues
- API host has long response time (around 15 seconds)
- inputs are not checked
