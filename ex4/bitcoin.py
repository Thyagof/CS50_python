import json
import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        amount = float(sys.argv[1])
    except:
        sys.exit(1)

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit(1)

    r = response.json()
    bitcoin = r["bpi"]["USD"]["rate_float"]
    total_amount = bitcoin * amount
    print(f"${total_amount:,.4f}")

if __name__ == "__main__":
    main()
