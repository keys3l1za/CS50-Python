import requests
import sys
import json

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except (requests.RequestException, json.JSONDecodeError) as e:
        raise e

def calculate_cost(n, bitcoin_price):
    try:
        n_bitcoin = float(n)
        cost = n_bitcoin * bitcoin_price
        return cost
    except ValueError:
        raise ValueError("Command-line argument is not a number")

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    n = sys.argv[1]

    try:
        bitcoin_price = get_bitcoin_price()
        cost = calculate_cost(n, bitcoin_price)
        formatted_cost = f"${cost:,.4f}"
        print(f"{n} Bitcoins == {formatted_cost} USD.")
    except (requests.RequestException, json.JSONDecodeError, ValueError) as e:
        print(f"{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
