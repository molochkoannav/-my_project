def filter_by_state(api_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует списки словарей по ключу 'state'"""
    filtered_api_list: list[dict] = []

    for api in api_list:
        if api.get("state") == state:
            filtered_api_list.append(api)

    return filtered_api_list


def sort_by_date(api_list: list[dict], sort_by: str = "date", reverse: bool = True) -> list[dict]:
    """Функция сортирует список словарей по дате."""
    return sorted(api_list, key=lambda date: date.get(sort_by, ""), reverse=reverse)
