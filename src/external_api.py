import os

from dotenv import load_dotenv
import requests
# from bs4 import BeautifulSoup


load_dotenv()

api_token = os.getenv("API_KEY")


def get_valute_transactions(transaction: dict)-> float:
    """ Функция для получения курса валют и конвертации суммы в рубли"""
    amount = float(transaction.get("operationAmount", {}).get("amount"))
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if currency_code == "RUB":
        return amount

    elif currency_code == "USD":
        url = "https://api.apilayer.com/exchangerates_data/latest?symbols=symbols&base=base"

        headers = {
            "apikey": api_token
        }
        response = requests.get(url, headers=headers)

        status_code = response.status_code
        result = response.json()
        # response = requests.get(f"https://api.currencylayer.com/convert?access_key={api_token}&from={currency_code}&to=RUB&amount={amount}")
        # result = response.json()
        return result, status_code
        # url = 'https://www.cbr.ru/currency_base/daily/'
        # response = requests.get(url)
        # soup = BeautifulSoup(response.text, 'html.parser') # Парсинг с сайта
        # table = soup.find('table', class_='data')
        #
        # for row in table.find_all('tr')[1:]:
        #     cols = row.find_all('td')
        #     if len(cols) >= 5 and cols[1].text == currency_code:
        #         rate = float(cols[4].text.replace(',', '.'))
        #         return round(amount * rate, 2)

    # elif currency_code == "EUR":
    #     response = requests.get(f"https://api.currencylayer.com/convert?access_key={api_token}&from={currency_code}&to=RUB&{amount}")
    #     result = response.json()
    #     return result
        # url = 'https://www.cbr.ru/currency_base/daily/' # Парсинг с сайта
        # response = requests.get(url)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # table = soup.find('table', class_='data')
        #
        # for row in table.find_all('tr')[1:]:
        #     cols = row.find_all('td')
        #     if len(cols) >= 5 and cols[1].text == currency_code:
        #         rate = float(cols[4].text.replace(',', '.'))
        #         return round(amount * rate, 2)
