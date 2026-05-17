
from unittest.mock import Mock
from unittest.mock import patch

import requests

from src.external_api import get_valute_transactions


class TestGetValuteTransactions:

    def test_rub_no_conversion_needed(self):
        """Тест для RUB - конвертация не нужна"""
        transaction = {"operationAmount": {"amount": "100.50", "currency": {"code": "RUB"}}}
        result = get_valute_transactions(transaction)
        assert result == 100.50

    def test_missing_currency_code(self):
        """Тест при отсутствии кода валюты"""
        transaction = {"operationAmount": {"amount": "100", "currency": {}}}
        result = get_valute_transactions(transaction)
        assert result == 0.0

    def test_missing_amount(self):
        """Тест при отсутствии суммы"""
        transaction = {"operationAmount": {"currency": {"code": "USD"}}}
        result = get_valute_transactions(transaction)
        assert result == 0.0

    @patch("requests.get")
    def test_usd_conversion_success(self, mock_get):
        """Тест успешной конвертации USD в RUB"""
        # Создаем мок-ответ
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"Valute": {"USD": {"Value": 92.50}}}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

        result = get_valute_transactions(transaction)
        # 100 USD * 92.50 = 9250.00
        assert result == 9250.00
        mock_get.assert_called_once_with("https://www.cbr-xml-daily.ru/daily_json.js")

    @patch("requests.get")
    def test_eur_conversion_success(self, mock_get):
        """Тест успешной конвертации EUR в RUB"""
        mock_response = Mock()
        mock_response.json.return_value = {"Valute": {"EUR": {"Value": 100.25}}}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        transaction = {"operationAmount": {"amount": "50", "currency": {"code": "EUR"}}}

        result = get_valute_transactions(transaction)
        # 50 EUR * 100.25 = 5012.50
        assert result == 5012.50

    @patch("requests.get")
    def test_api_request_error(self, mock_get):
        """Тест ошибки при запросе к API"""
        mock_get.side_effect = requests.RequestException("API Error")

        transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

        result = get_valute_transactions(transaction)
        assert result == 0.0

    @patch("requests.get")
    def test_missing_currency_in_response(self, mock_get):
        """Тест отсутствия курса валюты в ответе API"""
        mock_response = Mock()
        mock_response.json.return_value = {"Valute": {}}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

        result = get_valute_transactions(transaction)
        assert result is None or isinstance(result, (int, float))
