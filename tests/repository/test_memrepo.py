import pytest

from tripper.domain.elements import Station
from tripper.repository import memrepo


@pytest.fixture
def station_dicts():
    return [
        {'code': 'MEX', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None},
        {'code': 'GDL', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None},
        {'code': 'JFK', 'continent': 'America', 'tz_city': 'New_York', 'viaticum': None},
        {'code': 'MAD', 'continent': 'Europe', 'tz_city': 'Madrid', 'viaticum': None}
    ]


def test_repository_list_without_parameters(station_dicts):
    repo = memrepo.MemRepo(station_dicts)

    stations = [Station.from_dict(a) for a in station_dicts]

    assert repo.list() == stations


def test_repository_list_with_continent_equal_filter(station_dicts):
    repo = memrepo.MemRepo(station_dicts)

    repo_stations = repo.list(
        filters={'continent__eq': 'America'}
    )
    assert len(repo_stations) == 3
    assert repo_stations[0].continent == 'America'


def test_repository_list_with_codes_list_filter(station_dicts):
    repo = memrepo.MemRepo(station_dicts)

    repo_stations = repo.list(
        filters={'codes_list': ['MEX', 'MAD', 'GDL', 'JFK']}
    )
    assert len(repo_stations) == 4


def test_repository_list_with_tz_city_filter(station_dicts):
    repo = memrepo.MemRepo(data=station_dicts)

    repo_stations = repo.list(
        filters={'tz_city__eq': 'Mexico_City'}
    )
    assert len(repo_stations) == 2
    assert repo_stations[0].tz_city == 'Mexico_City'
    assert repo_stations[1].tz_city == 'Mexico_City'
