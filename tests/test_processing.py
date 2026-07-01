from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state(full_dict: list[dict], state_executed: list[dict], state_cenceled: list[dict]) -> None:
    """Функция для проверки корректности фильтрации по ключу state"""
    assert filter_by_state(full_dict, state="CANCELED") == state_cenceled
    assert filter_by_state(full_dict, state="EXECUTED") == state_executed


def test_sort_by_date(date_full_dict: list[dict], sort_flag_false: list[dict], sort_flag_true: list[dict]) -> None:
    """Функция для проверки корректности сортировке по дате"""
    assert sort_by_date(date_full_dict) == sort_flag_true
    assert sort_by_date(date_full_dict, reverse=False) == sort_flag_false
