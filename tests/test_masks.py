import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("123412341234123", "Номер карты набран не верно"),
        ("12341234123412345", "Номер карты набран не верно"),
        ("qw341234123!1234", "Номер карты набран не верно"),
        ("12 4123412 11234", "Номер карты набран не верно"),
        ("1234123412341234", "1234 12** **** 1234"),
        ("", "Номер карты набран не верно"),
        ("0000123412341234", "Номер карты набран не верно"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    """Функция для проверки правильности маскировки номера карты"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("736541084301358743051", "Номер счета набран не верно"),
        ("7365410843013587430", "Номер счета набран не верно"),
        ("736as1084301358743051", "Номер счета набран не верно"),
        ("7365410 43013587 3051", "Номер счета набран не верно"),
        ("73654108430135874305", "**4305"),
        ("", "Номер счета набран не верно"),
        ("00004108430135874305", "Номер счета набран не верно"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    """Функция для проверки правильности маскировки номера счета"""
    assert get_mask_account(account_number) == expected
