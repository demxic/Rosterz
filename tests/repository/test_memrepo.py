import pytest

from tripper.domain.elements import Station
from tripper.repository import memrepo


@pytest.fixture
def airport_dicts():
    return [
        {'code': 'MEX', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None},
        {'code': 'GDL', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None},
        {'code': 'JFK', 'continent': 'America', 'tz_city': 'New_York', 'viaticum': None},
        {'code': 'MAD', 'continent': 'Europe', 'tz_city': 'Madrid', 'viaticum': None}
    ]


def test_repository_list_without_parameters(airport_dicts):
    repo = memrepo.MemRepo(airport_dicts)

    airports = [Station.from_dict(a) for a in airport_dicts]
    assert repo.list() == airports
