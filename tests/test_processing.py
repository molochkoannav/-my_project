import pytest
from src.processing import filter_by_state


@pytest.mark.parametrize("dict_api, expected", [ ([
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ], [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ([{"id": 41428829, "state": " ", "date": "2019-07-03T18:35:29.512364"},
      {"id": 939719570, "date": "2018-06-30T02:08:58.425572"}], []),
    ([{'id': 414288292, 'state': 'PENDING', 'date': '2023-05-12T14:30:22.789012'},
    {'id': 414288293, 'state': 'IN_PROGRESS', 'date': '2024-01-20T09:45:10.345678'},
    {'id': 414288294, 'state': 'FAILED', 'date': '2022-11-07T22:15:33.987654'},
    {'id': 414288295, 'state': 'REVERSED', 'date': '2021-08-30T11:20:55.123789'},
    {'id': 414288296, 'state': 'WAITING', 'date': '2025-02-18T07:10:44.567890'},
    {'id': 414288297, 'state': 'COMPLETED', 'date': '2023-12-01T16:50:12.234567'},
    {'id': 414288298, 'state': 'EXPIRED', 'date': '2020-06-25T05:30:09.876543'},
    {'id': 414288299, 'state': 'ON_HOLD', 'date': '2024-03-14T19:40:21.456789'},
    {'id': 414288300, 'state': 'REFUNDED', 'date': '2022-09-03T13:55:47.998877'},
    {'id': 414288301, 'state': 'DECLINED', 'date': '2021-12-11T03:25:33.112233'},], [])
])
def test_filter_by_state(dict_api, expected):
    assert filter_by_state(dict_api) == expected
