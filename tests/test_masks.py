import pytest
from src.masks import get_mask_card_number

@pytest.mark.parametrize("card_number, expected", [
    ('123412341234123', 'Номер карты набран не верно'),
    ('12341234123412345', 'Номер карты набран не верно'),
    ('qw341234123!1234', 'Номер карты набран не верно'),
    ('12 4123412 11234', 'Номер карты набран не верно'),
    ('1234123412341234', '1234 12** **** 1234'),
    ('', 'Номер карты набран не верно')
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected