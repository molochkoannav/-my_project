from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция обрабатывает информацию как о картах, так и о счетах"""

    # СЧЕТ
    if number.startswith('Счет'):
        digits = ''.join(filter(str.isdigit, number))

        if len(digits) != 20:
            return "Номер счета набран не верно"
        if digits.startswith('0000'):
            return "Номер счета набран не верно"
        temp = number.replace('Счет', '').replace(' ', '')
        if not temp.isdigit() or len(temp) != 20:
            return "Номер счета набран не верно"

        account = get_mask_account(digits)
        return f"Счет {account}"

    # КАРТА

    digits_only = ''.join(filter(str.isdigit, number))
    if len(digits_only) == 20 and number.replace(' ', '').isdigit():
        account = get_mask_account(digits_only)
        return f"Счет {account}"

    name_part = ''
    for i, char in enumerate(number):
        if char.isdigit():
            name_part = number[:i].strip()
            card_part = number[i:]
            break
    else:
        return "Номер карты набран не верно"

    card_digits = card_part.replace(' ', '')

    if not card_digits.isdigit() or len(card_digits) != 16 or card_digits.startswith(('0', '00', '000', '0000')):
        return "Номер карты набран не верно"

    if not card_part.replace(' ', '').isdigit():
        return "Номер карты набран не верно"

    card_number = get_mask_card_number(card_digits)

    if name_part:
        return f"{name_part} {card_number}"
    return card_number


def get_date(data: str) -> str:
    """Функция конвертирует правильное обозначение даты ДД.ММ.ГГГГ"""
    data_time = data[:10].split("-")

    return f"{data_time[2]}.{data_time[1]}.{data_time[0]}"
