from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция обрабатывает информацию как о картах, так и о счетах"""

    # СЧЕТ
    if number.startswith("Счет"):
        digits = "".join(filter(str.isdigit, number))

        if len(digits) != 20:
            return "Номер счета набран не верно"
        if digits.startswith("0000"):
            return "Номер счета набран не верно"
        temp = number.replace("Счет", "").replace(" ", "")
        if not temp.isdigit() or len(temp) != 20:
            return "Номер счета набран не верно"

        account = get_mask_account(digits)
        return f"Счет {account}"

    # КАРТА

    digits_only = "".join(filter(str.isdigit, number))
    if len(digits_only) == 20 and number.replace(" ", "").isdigit():
        account = get_mask_account(digits_only)
        return f"Счет {account}"

    name_part = ""
    for i, char in enumerate(number):
        if char.isdigit():
            name_part = number[:i].strip()
            card_part = number[i:]
            break
    else:
        return "Номер карты набран не верно"

    card_digits = card_part.replace(" ", "")

    if not card_digits.isdigit() or len(card_digits) != 16 or card_digits.startswith(("0", "00", "000", "0000")):
        return "Номер карты набран не верно"

    if not card_part.replace(" ", "").isdigit():
        return "Номер карты набран не верно"

    card_number = get_mask_card_number(card_digits)

    if name_part:
        return f"{name_part} {card_number}"
    return card_number


def get_date(date_string: str) -> str:
    """
    Преобразует разные форматы даты в ДД.ММ.ГГГГ
    """

    date_string = date_string.strip()

    # Формат: ГГГГ-ММ-ДД
    try:
        dt = datetime.strptime(date_string, "%Y-%m-%d")
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        pass

    # ISO формат 2024-03-11T02:26:18.671407
    try:
        if "T" in date_string and "." in date_string:
            date_string_clean = date_string.split(".")[0]
            dt = datetime.strptime(date_string_clean, "%Y-%m-%dT%H:%M:%S")
            return dt.strftime("%d.%m.%Y")
    except ValueError:
        pass

    # ISO формат 2024-03-11T02:26:18
    try:
        dt = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        pass

    # Формат: ММ/ДД/ГГГГ (американский)
    try:
        dt = datetime.strptime(date_string, "%m/%d/%Y")
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        pass

    # Формат: ДД.ММ.ГГГГ
    try:
        dt = datetime.strptime(date_string, "%d.%m.%Y")
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        pass

    # Формат: ДД-ММ-ГГГГ
    try:
        dt = datetime.strptime(date_string, "%d-%m-%Y")
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        pass

    # Формат: ДД/ММ/ГГГГ
    try:
        dt = datetime.strptime(date_string, "%d/%m/%Y")
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        pass

    # Формат: Месяц ДД, ГГГГ
    try:
        dt = datetime.strptime(date_string, "%B %d, %Y")
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        pass

    # Формат: Месяц ДД ГГГГ
    try:
        dt = datetime.strptime(date_string, "%B %d %Y")
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        pass

    # Формат: ДД Месяц ГГГГ
    try:
        dt = datetime.strptime(date_string, "%d %B %Y")
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        pass

    return "Ошибка: неверный формат даты"
