from typing import Union


def get_mask_card_number(cart_number: Union[int]) -> Union[str]:
    """Функция маскирует номер карты пользователя"""
    list_cart_number = [number for number in (str(cart_number))]
    list_cart_number[6:-4] = ["*", "*", "*", "*", "*", "*"]
    for num in range(len(list_cart_number) // 4 - 1, 0, -1):
        list_cart_number[num * 4: num * 4] = [" "]

    mask_cart_number = "".join(list_cart_number)
    return mask_cart_number


def get_mask_account(account_number: Union[int]) -> Union[str]:
    """Функция маскирует номер счета пользователя"""
    list_account_number = [number for number in (str(account_number))]
    list_account_number[:-4] = ["*", "*"]
    mask_account = "".join(list_account_number)

    return mask_account

