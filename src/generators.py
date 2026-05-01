from collections.abc import Generator
from typing import Any


def filter_by_currency(transactions: list[dict], cur: str = "USD") -> Generator[dict[Any, Any] | str]:
    """Функция фильтрует id по типу валюты (по умолчанию - USD)"""
    filtered = [
        item
        for item in transactions
        if isinstance(item, dict) and item.get("operationAmount", {}).get("currency", {}).get("code") == cur
    ]

    yield from (item if item else "Словарь пуст" for item in filtered)


def transaction_descriptions(transactions: list[dict]) -> Generator[dict, None, None]:
    """Функция возвращает описание каждой операции."""
    for api in transactions:
        yield api["description"]


def card_number_generator(start_num: int, stop_num: int) -> Generator[str, None, None]:
    """Функция которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for current in range(start_num, stop_num + 1):
        num = str(current).zfill(16)
        card_num = " ".join(num[i: i + 4] for i in range(0, 16, 4))
        yield card_num
