import pytest
from datetime import datetime

import pytz

from tripper.domain.interval import Interval
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
        {'name': '0224', 'origin': station_dicts[0], 'destination': station_dicts[1], 'id': 3},
        {'name': '0401', 'origin': station_dicts[2], 'destination': station_dicts[0], 'id': 4}
    ]


@pytest.fixture(scope='module')
def domain_routes(route_dicts):
    return [Route.from_dict(a_dict=a_dict) for a_dict in route_dicts]


@pytest.fixture(scope='module')
def interval_dicts():
    return [
            [dict(year=2019, month=11, day=2, hour=00, minute=45),
             dict(year=2019, month=11, day=2, hour=11, minute=30)],
            [dict(year=2019, month=11, day=21, hour=23, minute=0),
             dict(year=2019, month=11, day=22, hour=2, minute=30)],
            [dict(year=2019, month=12, day=1, hour=12, minute=0),
             dict(year=2019, month=12, day=2, hour=18, minute=0)]
            ]


@pytest.fixture(scope='module')
def domain_intervals(interval_dicts):
    """ Interval 0: 0001 MEX MAD
        Interval 1: 0224 MEX GDL
        Interval 3:   T1 MEX MEX"""
    utc = pytz.UTC
    return [Interval(begin=utc.localize(datetime(**interval_dicts[0][0])),
                     end=utc.localize(datetime(**interval_dicts[0][1]))),
            Interval(begin=utc.localize(datetime(**interval_dicts[1][0])),
                     end=utc.localize(datetime(**interval_dicts[1][1]))),
            Interval(begin=utc.localize(datetime(**interval_dicts[2][0])),
                     end=utc.localize(datetime(**interval_dicts[2][1])))
            ]
