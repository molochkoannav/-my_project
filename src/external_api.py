import os
from locale import currency

from dotenv import load_dotenv
import requests


load_dotenv()

api_token = os.getenv("API_KEY")

def get_valute_transactions(transaction: dict)-> float:
    if transaction["operationAmount"]["amount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        url = f"https://api.currencyfreaks.com/v2.0/rates/latest?{api_token}"
        response =