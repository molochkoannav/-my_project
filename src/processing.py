def filter_by_state(api_list: list[dict], state: str) -> list[dict]:
    """Функция фильтрует списки словарей по ключу 'state'"""
    try:
        filtered_api_list: list[dict] = []

        for api in api_list:
            if api.get("state") == state:
                filtered_api_list.append(api)
        return filtered_api_list
    except KeyError, ValueError:
        return []



def sort_by_date(api_list: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортирует список словарей по дате."""
    return sorted(api_list, key=lambda date: date.get("date", ""), reverse=reverse)
