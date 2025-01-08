import requests
import sys
if len(sys.argv) !=2:
    sys.exit("Missing command-line argument")

if sys.argv[1].isdigit()==False:
    sys.exit("Command-line argument is not a number")
try:
    r=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    f = response["bpi"]["USD"]["rate_float"]

    value=float(sys.argv[1])
    price = float(f)*value
    print(f"${price:,}", end="")
except requests.RequestException:
    pass
