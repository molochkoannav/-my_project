from pathlib import Path
from unittest.mock import Mock
from unittest.mock import patch

import pandas as pd
import pytest

from src.data_loader import csv_reader
from src.data_loader import excel_reader


@patch("src.data_loader.pd.read_csv")
def test_csv_reader_success(mock_read_csv):
    """Тестируем функцию csv_reader при успешном чтении"""

    mock_df = Mock()
    mock_df.set_index.return_value = mock_df
    mock_df.to_dict.return_value = [
        {
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]

    mock_read_csv.return_value = mock_df

    file_path = Path("data.csv")
    result = csv_reader(file_path)

    assert len(result) == 2
    assert result[0]["amount"] == 16210.0
    assert result[1]["amount"] == 29740.0
    assert result[0]["state"] == "EXECUTED"

    mock_read_csv.assert_called_once_with(file_path, delimiter=";", encoding="utf-8")
    mock_df.set_index.assert_called_once_with("id", inplace=True)
    mock_df.to_dict.assert_called_once_with(orient="records")


@patch("src.data_loader.pd.read_csv")
def test_missing_csv_file(mock_read_csv):
    """Тест при отсутствии файла и ошибке FileNotFoundError"""
    mock_read_csv.side_effect = FileNotFoundError()
    with pytest.raises(FileNotFoundError):
        csv_reader(Path("any_file.csv"))


@patch("src.data_loader.pd.read_csv")
def test_empty_csv_file(mock_read_csv):
    """Тест при ошибке pd.errors.EmptyDataError"""
    mock_read_csv.side_effect = pd.errors.EmptyDataError
    with pytest.raises(pd.errors.EmptyDataError):
        csv_reader(Path("any_file.csv"))


@patch("src.data_loader.pd.read_csv")
def test_unknown_exception(mock_read_csv):
    """Тест при ошибке Exception"""
    mock_read_csv.side_effect = Exception
    with pytest.raises(Exception):
        csv_reader(Path("any_file.csv"))


@patch("src.data_loader.pd.read_excel")
def test_excel_reader_success(mock_read_excel):
    """Тестируем функцию excel_reader при успешном чтении"""

    mock_df = Mock()
    mock_df.set_index.return_value = mock_df
    mock_df.to_dict.return_value = [
        {
            "state": "EXECUTED",
            "date": "2022-04-14T15:14:21Z",
            "amount": 24853.0,
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Счет 38577962752140632721",
            "to": "Счет 47657753885349826314",
            "description": "Перевод со счета на счет",
        },
        {
            "state": "EXECUTED",
            "date": "2023-01-04T13:13:34Z",
            "amount": 15560.0,
            "currency_name": "Real",
            "currency_code": "BRL",
            "from": "Счет 38577962752140632721",
            "to": "Счет 38164279390569873521",
            "description": "Открытие вклада",
        },
        {
            "state": "EXECUTED",
            "date": "2022-03-23T08:29:37Z",
            "amount": 23423.0,
            "currency_name": "Peso",
            "currency_code": "PHP",
            "from": "Discover 7269000803370165",
            "to": "American Express 1963030970727681",
            "description": "Перевод с карты на карту",
        },
    ]

    mock_read_excel.return_value = mock_df

    file_path = Path("data.excel")
    result = excel_reader(file_path)

    assert len(result) == 3
    assert result[0]["amount"] == 24853.0
    assert result[1]["amount"] == 15560.0
    assert result[0]["state"] == "EXECUTED"

    mock_read_excel.assert_called_once_with(file_path)
    mock_df.set_index.assert_called_once_with("id", inplace=True)
    mock_df.to_dict.assert_called_once_with(orient="records")


@patch("src.data_loader.pd.read_excel")
def test_missing_excel_file(mock_read_excel):
    """Тест при отсутствии файла и ошибке FileNotFoundError"""
    mock_read_excel.side_effect = FileNotFoundError()
    with pytest.raises(FileNotFoundError):
        excel_reader(Path("any_file.xlsx"))


@patch("src.data_loader.pd.read_excel")
def test_empty_excel_file(mock_read_excel):
    """Тест при отсутствии ошибке pd.errors.EmptyDataError"""
    mock_read_excel.side_effect = pd.errors.EmptyDataError
    with pytest.raises(pd.errors.EmptyDataError):
        excel_reader(Path("any_file.xlsx"))


@patch("src.data_loader.pd.read_excel")
def test_unknown_exception_in_excel(mock_read_excel):
    """Тест при отсутствии ошибке Exception"""
    mock_read_excel.side_effect = Exception
    with pytest.raises(Exception):
        excel_reader(Path("any_file.xlsx"))
