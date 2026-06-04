import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import main


@patch('builtins.input')
@patch('main.get_read_transactions')
@patch('main.filter_by_state')
@patch('main.sort_by_date')
@patch('main.filter_by_currency')
@patch('main.process_bank_search')
@patch('main.mask_account_card')
@patch('main.get_date')
def test_main_json_success(
    mock_get_date,
    mock_mask_card,
    mock_search,
    mock_filter_currency,
    mock_sort_date,
    mock_filter_state,
    mock_get_transactions,
    mock_input
):
    mock_get_transactions.return_value = [{
        "id": 1,
        "state": "EXECUTED",
        "date": "2024-01-15T10:00:00Z",
        "description": "Test transaction",
        "operationAmount": {
            "amount": "1000",
            "currency": {
                "name": "рубль",
                "code": "RUB"
            }
        },
        "from": "1234567890",
        "to": "0987654321"
    }]

    transformed_data = [{
        "id": 1,
        "state": "EXECUTED",
        "date": "2024-01-15T10:00:00Z",
        "amount": "1000",
        "currency_name": "рубль",
        "currency_code": "RUB",
        "description": "Test transaction",
        "from": "1234567890",
        "to": "0987654321"
    }]

    mock_filter_state.return_value = transformed_data
    mock_sort_date.return_value = transformed_data
    mock_filter_currency.return_value = transformed_data
    mock_search.return_value = transformed_data
    mock_mask_card.side_effect = lambda x: f"****{x[-4:]}" if x else ""
    mock_get_date.return_value = "15.01.2024"

    mock_input.side_effect = [
        "1",
        "EXECUTED",
        "нет",
        "нет",
        "нет"
    ]

    main()
    mock_get_transactions.assert_called_once_with("data/operations.json")
    mock_filter_state.assert_called_once()


@patch('builtins.input')
@patch('main.csv_reader')
@patch('main.filter_by_state')
@patch('main.get_date')
@patch('main.mask_account_card')
def test_main_csv(mock_mask_card, mock_get_date, mock_filter_state, mock_csv_reader, mock_input):
    mock_csv_reader.return_value = [{
        "id": 1,
        "state": "EXECUTED",
        "date": "2024-01-15T10:00:00Z",
        "description": "Test",
        "amount": "500",
        "currency_code": "USD",
        "from": "1234567890",
        "to": "0987654321"
    }]
    mock_filter_state.return_value = mock_csv_reader.return_value
    mock_get_date.return_value = "15.01.2024"
    mock_mask_card.side_effect = lambda x: f"****{x[-4:]}" if x else ""

    mock_input.side_effect = [
        "2",
        "EXECUTED",
        "нет",
        "нет",
        "нет"
    ]

    main()
    mock_csv_reader.assert_called_once_with("data/transactions.csv")


@patch('builtins.input')
@patch('main.excel_reader')
@patch('main.filter_by_state')
@patch('main.get_date')
@patch('main.mask_account_card')
def test_main_excel(mock_mask_card, mock_get_date, mock_filter_state, mock_excel_reader, mock_input):
    mock_excel_reader.return_value = [{
        "id": 1,
        "state": "EXECUTED",
        "date": "2024-01-15T10:00:00Z",
        "description": "Test",
        "amount": "1000",
        "currency_code": "RUB",
        "from": "1234567890",
        "to": "0987654321"
    }]
    mock_filter_state.return_value = mock_excel_reader.return_value
    mock_get_date.return_value = "15.01.2024"
    mock_mask_card.side_effect = lambda x: f"****{x[-4:]}" if x else ""

    mock_input.side_effect = [
        "3",
        "EXECUTED",
        "нет",
        "нет",
        "нет"
    ]

    main()
    mock_excel_reader.assert_called_once_with("data/transactions_excel.xlsx")


@patch('builtins.input')
@patch('main.get_read_transactions')
@patch('main.filter_by_state')
@patch('main.get_date')
@patch('main.mask_account_card')
def test_main_invalid_menu_choice(mock_mask_card, mock_get_date, mock_filter_state, mock_get_transactions, mock_input):
    mock_get_transactions.return_value = [{
        "id": 1,
        "state": "EXECUTED",
        "date": "2024-01-15T10:00:00Z",
        "description": "Test transaction",
        "operationAmount": {
            "amount": "1000",
            "currency": {"code": "RUB"}
        },
        "from": "1234567890",
        "to": "0987654321"
    }]

    transformed_data = [{
        "id": 1,
        "state": "EXECUTED",
        "date": "2024-01-15T10:00:00Z",
        "amount": "1000",
        "currency_code": "RUB",
        "description": "Test transaction",
        "from": "1234567890",
        "to": "0987654321"
    }]

    mock_filter_state.return_value = transformed_data
    mock_get_date.return_value = "15.01.2024"
    mock_mask_card.side_effect = lambda x: f"****{x[-4:]}" if x else ""

    mock_input.side_effect = [
        "5",
        "1",
        "EXECUTED",
        "нет",
        "нет",
        "нет"
    ]

    main()
    mock_get_transactions.assert_called_once()


@patch('builtins.input')
@patch('main.get_read_transactions')
@patch('main.filter_by_state')
@patch('main.get_date')
@patch('main.mask_account_card')
def test_main_invalid_status(mock_mask_card, mock_get_date, mock_filter_state, mock_get_transactions, mock_input):
    mock_get_transactions.return_value = [{
        "id": 1,
        "state": "EXECUTED",
        "date": "2024-01-15T10:00:00Z",
        "description": "Test transaction",
        "operationAmount": {
            "amount": "1000",
            "currency": {
                "name": "рубль",
                "code": "RUB"
            }
        },
        "from": "1234567890",
        "to": "0987654321"
    }]

    transformed_data = [{
        "id": 1,
        "state": "EXECUTED",
        "date": "2024-01-15T10:00:00Z",
        "amount": "1000",
        "currency_name": "рубль",
        "currency_code": "RUB",
        "description": "Test transaction",
        "from": "1234567890",
        "to": "0987654321"
    }]

    mock_filter_state.return_value = transformed_data
    mock_get_date.return_value = "15.01.2024"
    mock_mask_card.side_effect = lambda x: f"****{x[-4:]}" if x else ""

    mock_input.side_effect = [
        "1",
        "INVALID",
        "EXECUTED",
        "нет",
        "нет",
        "нет"
    ]

    main()
    mock_filter_state.assert_called_with(transformed_data, "EXECUTED")


@patch('builtins.input')
@patch('main.get_read_transactions')
@patch('main.filter_by_state')
@patch('main.sort_by_date')
@patch('main.get_date')
@patch('main.mask_account_card')
def test_main_sort_descending(mock_mask_card, mock_get_date, mock_sort_date, mock_filter_state, mock_get_transactions, mock_input):
    mock_get_transactions.return_value = [{
        "id": 1,
        "date": "2024-01-15T10:00:00Z",
        "state": "EXECUTED",
        "description": "Test transaction",
        "operationAmount": {
            "amount": "1000",
            "currency": {"code": "RUB"}
        },
        "from": "1234567890",
        "to": "0987654321"
    }]

    transformed_data = [{
        "id": 1,
        "date": "2024-01-15T10:00:00Z",
        "state": "EXECUTED",
        "amount": "1000",
        "currency_code": "RUB",
        "description": "Test transaction",
        "from": "1234567890",
        "to": "0987654321"
    }]

    mock_filter_state.return_value = transformed_data
    mock_sort_date.return_value = transformed_data
    mock_get_date.return_value = "15.01.2024"
    mock_mask_card.side_effect = lambda x: f"****{x[-4:]}" if x else ""

    mock_input.side_effect = [
        "1",
        "EXECUTED",
        "да",
        "по убыванию",
        "нет",
        "нет"
    ]

    main()
    mock_sort_date.assert_called_with(mock_filter_state.return_value)


@patch('builtins.input')
@patch('main.get_read_transactions')
@patch('main.filter_by_state')
@patch('main.sort_by_date')
@patch('main.get_date')
@patch('main.mask_account_card')
def test_main_sort_ascending(mock_mask_card, mock_get_date, mock_sort_date, mock_filter_state, mock_get_transactions, mock_input):
    mock_get_transactions.return_value = [{
        "id": 1,
        "date": "2024-01-15T10:00:00Z",
        "state": "EXECUTED",
        "description": "Test transaction",
        "operationAmount": {
            "amount": "1000",
            "currency": {"code": "RUB"}
        },
        "from": "1234567890",
        "to": "0987654321"
    }]

    transformed_data = [{
        "id": 1,
        "date": "2024-01-15T10:00:00Z",
        "state": "EXECUTED",
        "amount": "1000",
        "currency_code": "RUB",
        "description": "Test transaction",
        "from": "1234567890",
        "to": "0987654321"
    }]

    mock_filter_state.return_value = transformed_data
    mock_sort_date.return_value = transformed_data
    mock_get_date.return_value = "15.01.2024"
    mock_mask_card.side_effect = lambda x: f"****{x[-4:]}" if x else ""

    mock_input.side_effect = [
        "1",
        "EXECUTED",
        "да",
        "по возрастанию",
        "нет",
        "нет"
    ]

    main()
    mock_sort_date.assert_called_with(mock_filter_state.return_value, reverse=False)


@patch('builtins.input')
@patch('main.get_read_transactions')
@patch('main.filter_by_state')
@patch('main.filter_by_currency')
@patch('main.get_date')
@patch('main.mask_account_card')
def test_main_filter_rub(mock_mask_card, mock_get_date, mock_filter_currency, mock_filter_state, mock_get_transactions, mock_input):
    mock_get_transactions.return_value = [{
        "id": 1,
        "state": "EXECUTED",
        "date": "2024-01-15T10:00:00Z",
        "description": "Test transaction",
        "operationAmount": {
            "amount": "1000",
            "currency": {"code": "RUB"}
        },
        "from": "1234567890",
        "to": "0987654321"
    }]

    transformed_data = [{
        "id": 1,
        "date": "2024-01-15T10:00:00Z",
        "state": "EXECUTED",
        "amount": "1000",
        "currency_code": "RUB",
        "description": "Test transaction",
        "from": "1234567890",
        "to": "0987654321"
    }]

    mock_filter_state.return_value = transformed_data
    mock_filter_currency.return_value = transformed_data
    mock_get_date.return_value = "15.01.2024"
    mock_mask_card.side_effect = lambda x: f"****{x[-4:]}" if x else ""

    mock_input.side_effect = [
        "1",
        "EXECUTED",
        "нет",
        "да",
        "нет"
    ]

    main()
    mock_filter_currency.assert_called_with(mock_filter_state.return_value, "RUB")


@patch('builtins.input')
@patch('main.get_read_transactions')
@patch('main.filter_by_state')
@patch('main.process_bank_search')
@patch('main.get_date')
@patch('main.mask_account_card')
def test_main_search_description(mock_mask_card, mock_get_date, mock_search, mock_filter_state, mock_get_transactions, mock_input):
    mock_get_transactions.return_value = [{
        "id": 1,
        "description": "Покупка продуктов",
        "date": "2024-01-15T10:00:00Z",
        "state": "EXECUTED",
        "operationAmount": {
            "amount": "1000",
            "currency": {"code": "RUB"}
        },
        "from": "1234567890",
        "to": "0987654321"
    }]

    transformed_data = [{
        "id": 1,
        "date": "2024-01-15T10:00:00Z",
        "state": "EXECUTED",
        "amount": "1000",
        "currency_code": "RUB",
        "description": "Покупка продуктов",
        "from": "1234567890",
        "to": "0987654321"
    }]

    mock_filter_state.return_value = transformed_data
    mock_search.return_value = transformed_data
    mock_get_date.return_value = "15.01.2024"
    mock_mask_card.side_effect = lambda x: f"****{x[-4:]}" if x else ""

    mock_input.side_effect = [
        "1",
        "EXECUTED",
        "нет",
        "нет",
        "да",
        "продукты"
    ]

    main()
    mock_search.assert_called_with(mock_filter_state.return_value, "продукты")


@patch('builtins.input')
@patch('main.get_read_transactions')
@patch('main.filter_by_state')
@patch('main.filter_by_currency')
def test_main_empty_result(mock_filter_currency, mock_filter_state, mock_get_transactions, mock_input):
    mock_get_transactions.return_value = [{
        "id": 1,
        "date": "2024-01-15T10:00:00Z",
        "description": "Test transaction",
        "operationAmount": {
            "amount": "1000",
            "currency": {"code": "RUB"}
        }
    }]

    transformed_data = [{
        "id": 1,
        "date": "2024-01-15T10:00:00Z",
        "amount": "1000",
        "currency_code": "RUB",
        "description": "Test transaction"
    }]

    mock_filter_state.return_value = []
    mock_filter_currency.return_value = []

    mock_input.side_effect = [
        "1",
        "EXECUTED",
        "нет",
        "да",
        "нет"
    ]

    main()