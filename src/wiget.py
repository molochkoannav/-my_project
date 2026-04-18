from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(number: str) -> str:
    """функция обрабатывает информацию как о картах, так и о счетах"""
    if "счет" in number.lower():
        account = get_mask_account(int(number[-20:]))

        return f"Счет {account}"

    card_number = get_mask_card_number(int(number[-16:]))

    return f"{number[:-17]} {card_number}"


def get_date(data: str) -> str:
    """Фуенуия конвертирует правильное обозначение даты ДД.ММ.ГГГГ"""
    data_time = data[:10].split("-")

    return f"{data_time[2]}.{data_time[1]}.{data_time[0]}"

