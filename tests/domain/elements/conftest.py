import pytest

from tripper.domain.elements import Station, Route


@pytest.fixture(scope='module')
def station_dicts():
    return [
        {'code': 'MEX', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None},
        {'code': 'GDL', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None},
        {'code': 'JFK', 'continent': 'America', 'tz_city': 'New_York', 'viaticum': None},
        {'code': 'MAD', 'continent': 'Europe', 'tz_city': 'Madrid', 'viaticum': None}
    ]


@pytest.fixture(scope='module')
def domain_stations(station_dicts):
    return [Station.from_dict(a_dict=a_dict) for a_dict in station_dicts]


@pytest.fixture(scope='module')
def route_dicts(station_dicts):
    return [
        {'name': 'T1', 'origin': station_dicts[0], 'destination': station_dicts[0], 'id': 1},
        {'name': '0001', 'origin': station_dicts[3], 'destination': station_dicts[3], 'id': 2},
        {'name': '0106', 'origin': station_dicts[0], 'destination': station_dicts[1], 'id': 3},
        {'name': '0401', 'origin': station_dicts[2], 'destination': station_dicts[0], 'id': 4}
    ]


@pytest.fixture(scope='module')
def domain_routes(route_dicts):
    return [Route.from_dict(a_dict=a_dict) for a_dict in route_dicts]

