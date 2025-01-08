import requests
import json
import sys
url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_mXLvk2h5SbdS9UqlzIh9hqlRVunPthuIl9hAHC41"
def main():
    global url
    print("Supported Currencies: ")
    while True:

        try:
            currency = input("Currency: ")
            hm=input("How many? ")
            request = requests.get(url).json()
            value=request["data"][curren(currency)]
            total=howmany(hm)*val(value)
            print(f"{total}",curren(currency))
            sys.exit()
        except KeyError:
            print("ERROR: input not valid ")
            continue


def curren(currency):

    return currency.upper()
def howmany(hm):

    return int(hm)
def val(value):
    return float(value)

