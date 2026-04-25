from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция обрабатывает информацию как о картах, так и о счетах"""

    last_part = number[-20:] if len(number) >= 20 else ""

    if last_part.isdigit():
        account = get_mask_account(last_part)
        if account == "Номер счета набран не верно":
            return "Номер счета набран не верно"
        return f"Счет {account}"
    else:
        if len(number) < 16:
            return "Номер карты набран не верно"

        card_number = get_mask_card_number(number[-16:])
        if card_number == "Номер карты набран не верно":
            return "Номер карты набран не верно"
        return f"{number[:-16]}{card_number}"

def get_date(data: str) -> str:
    """Функция конвертирует правильное обозначение даты ДД.ММ.ГГГГ"""
    data_time = data[:10].split("-")

    return f"{data_time[2]}.{data_time[1]}.{data_time[0]}"
