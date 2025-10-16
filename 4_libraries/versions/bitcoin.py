
#Problem 6, version 1
"""
import sys
import requests
import json

if len(sys.argv) < 2:
    sys.exit("Missing command-line-argument")
elif len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=0aa4ab1cde6a82e9ee470d62e57620dfef7b918241d562e079a8900f5a767359")
        o = response.json()
        conversion_usd = float(o["data"]["priceUsd"])
        price_in_usd = n * conversion_usd

        print(f"${price_in_usd:,.4f}")

    except (ValueError,requests.RequestException):
        sys.exit("Something went wrong.")
"""
#version 2:
import sys
import requests

if len(sys.argv) != 2:                             #changed here.
    sys.exit("Missing command-line-argument")
elif len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=0aa4ab1cde6a82e9ee470d62e57620dfef7b918241d562e079a8900f5a767359")
        o = response.json()
        conversion_usd = float(o["data"]["priceUsd"])
        price_in_usd = n * conversion_usd

        print(f"${price_in_usd:,.4f}")

    except ValueError:
        sys.exit("Command line argument is not a number.")
    except requests.RequestException:
        sys.exit("API request failed.")