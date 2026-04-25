from string import digits
from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция маскирует номер карты пользователя"""
    if len(card_number) == 16 and card_number.isdigit():
            list_card_number = [number for number in (str(card_number))]
            list_card_number[6:-4] = ["*", "*", "*", "*", "*", "*"]
            for num in range(len(list_card_number) // 4 - 1, 0, -1):
                list_card_number[num * 4: num * 4] = [" "]

            mask_card_number = "".join(list_card_number)
            return mask_card_number

    else:
        return "Номер карты набран не верно"
def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция маскирует номер счета пользователя"""
    if len(account_number) == 20 and account_number.isdigit():
        list_account_number = [number for number in (str(account_number))]
        list_account_number[:-4] = ["*", "*"]
        mask_account = "".join(list_account_number)

        return mask_account
    else:
        return "Номер счета набран не верно"
