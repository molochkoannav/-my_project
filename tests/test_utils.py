import json

from unittest.mock import mock_open, patch
from src.utils import get_read_transactions  # добавлен load_transactions


class TestLoadTransactionsWithMocks:

    def test_get_valute_transactions(self):
        """Тест с моком файла"""
        mock_data = [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": 1000.00,
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                }
            }
        ]

        mock_file = mock_open(read_data=json.dumps(mock_data))

        with patch('builtins.open', mock_file):
            with patch('pathlib.Path.exists', return_value=True):
                result = get_read_transactions("/fake/path.json")

                assert len(result) == 1
                assert result[0]["operationAmount"]["amount"] == 1000.00
                assert result[0]["id"] == 441945886
                assert result[0]["operationAmount"]["currency"]["code"] == "RUB"
                mock_file.assert_called_once()

    def test_file_not_found_returns_empty_list(self):
        """Тест: при отсутствии файла возвращается пустой список (НЕ исключение)"""
        with patch('builtins.open', side_effect=FileNotFoundError):
            result = get_read_transactions("/nonexistent/file.json")


            assert isinstance(result, list)
            assert result == []

    def test_invalid_json_returns_empty_list(self):
        """Тест: при некорректном JSON возвращается пустой список"""
        mock_file = mock_open(read_data="json.decoder.JSONDecodeError:")

        with patch('builtins.open', mock_file):
            result = get_read_transactions("/fake/path.json")


            assert result == []

    def test_empty_list_returns_empty_list(self):
        """Тест: когда JSON - пустой список, возвращается пустой список"""
        mock_file = mock_open(read_data="[]")

        with patch('builtins.open', mock_file):
            result = get_read_transactions("/fake/path.json")

            assert result == []

    def test_value_error_returns_empty_list(self):
        """Тест: при ValueError возвращается пустой список"""
        with patch('builtins.open', side_effect=ValueError("Some error")):
            result = get_read_transactions("/fake/path.json")

            assert result == []