from collections.abc import Generator

def filter_by_currency(transactions: list[dict], cur: str = "USD") -> Generator[dict, None, None]:
    """Функция фильтрует id по типу валюты (по умолчанию - USD)"""
    yield from (api for api in transactions if api.get("operationAmount", {}).get("currency", {}).get("code") == cur)



def transaction_descriptions(transactions: list[dict])-> Generator[dict, None, None]:
    for api in transactions:
        yield api["description"]

def card_number_generator(start_num: int, stop_num: int)-> Generator[str, None, None]:
    for current in range(start_num, stop_num + 1):
        num = str(current).zfill(16)
        card_num = ' '.join(num[i:i + 4] for i in range(0, 16, 4))
        yield card_num


