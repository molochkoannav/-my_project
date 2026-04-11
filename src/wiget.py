from src.masks import get_mask_card_number, get_mask_account

def mask_account_card (number: str) -> str:
    if "счет" in number.lower():
        account = get_mask_account(int(number[-20:]))

        return f'Счет {account}'

    card_number = get_mask_card_number(int(number[-16:]))

    return f'{number[:-17]} {card_number}'


def get_date(data: str) -> str:
    data_time = data[:10].split("-")

    return f'{data_time[2]}.{data_time[1]}.{data_time[0]}'


if __name__ == '__main__':
    # print(mask_account_card("Maestro 1596837868705199"))
    # print(mask_account_card("Счет 64686473678894779589"))
    # print(mask_account_card("MasterCard 7158300734726758"))
    # print(mask_account_card("Visa Classic 6831982476737658"))
    # print(mask_account_card("Visa Platinum 8990922113665229"))
    # print(mask_account_card("Visa Gold 5999414228426353"))
    # print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))

