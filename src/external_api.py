
import requests


def get_valute_transactions(transaction: dict)-> float:
    """ Функция для получения курса валют и конвертации суммы в рубли"""
    amount = float(transaction.get("operationAmount", {}).get("amount"))
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if not currency_code or not amount:
        return 0.0

    if currency_code == "RUB":
        return amount

    elif currency_code == "USD":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        usd_amount = data.get("Valute", {}).get("USD", {}).get("Value")
        return round(amount * usd_amount, 2)


    elif currency_code == "EUR":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        usd_amount = data.get("Valute", {}).get("EUR", {}).get("Value")
        return round(amount * usd_amount, 2)

