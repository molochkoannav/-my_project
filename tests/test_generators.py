from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


def test_filter_by_currency(
    all_currency: list[dict],
    usd_one_currency: list[dict],
    usd_two_currency: list[dict],
    usd_three_currency: list[dict],
    no_required_currency: list[dict],
) -> None:
    """Функция для проверки генератора фильтрации списков"""

    expected = filter_by_currency(all_currency, cur="USD")
    result = list(expected)
    assert len(result) == 3
    assert result[0] == usd_one_currency[0]
    assert result[1] == usd_two_currency[0]
    assert result[2] == usd_three_currency[0]

    result = filter_by_currency([], "USD")
    result_list = list(result)
    assert len(result_list) == 0


def test_transaction_descriptions(all_currency: list[dict], empty_list: list) -> None:
    """Функция для проверки генератора вывода описания операции"""
    expected_1 = transaction_descriptions(all_currency)
    assert next(expected_1) == "Перевод организации"
    assert next(expected_1) == "Перевод со счета на счет"
    expected_2 = transaction_descriptions(empty_list)
    assert next(expected_2, None) is None


def test_card_number_generator() -> None:
    """Функция для проверки правильности генерации номера карты"""
    generator = card_number_generator(1, 3)
    generator_1 = card_number_generator(0, 1)
    generator_2 = card_number_generator(10, 11)
    generator_3 = card_number_generator(1000000000000000, 1100000000000000)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator_1) == "0000 0000 0000 0000"
    assert next(generator_1) == "0000 0000 0000 0001"
    assert next(generator_2) == "0000 0000 0000 0010"
    assert next(generator_2) == "0000 0000 0000 0011"
    assert next(generator_3) == "1000 0000 0000 0000"
    assert next(generator_3) == "1000 0000 0000 0001"
