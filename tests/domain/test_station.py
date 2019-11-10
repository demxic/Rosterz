import pytz
from tripper.domain.elements import Station


def test_station_model_init(domain_stations):
    station_mex = domain_stations[0]
    assert station_mex.code == 'MEX'
    assert station_mex.continent == 'America'
    assert station_mex.tz_city == 'Mexico_City'
    assert station_mex.viaticum is None
    assert station_mex.timezone == pytz.timezone('America/Mexico_City')


def test_station_model_from_dict():
    station_dict = {'code': 'station_mex', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None}
    station = Station.from_dict(station_dict)
    assert station.code == 'station_mex'
    assert station.continent == 'America'
    assert station.tz_city == 'Mexico_City'
    assert station.viaticum is None
    assert station.timezone == pytz.timezone('America/Mexico_City')


def test_station_model_to_dict(station_dicts):
    station_dict = station_dicts[0]
    station = Station.from_dict(station_dict)
    assert station.to_dict() == station_dict


def test_station_model_str(domain_stations):
    station_mex = domain_stations[0]
    expected_result = 'MEX'
    assert str(station_mex) == expected_result


def test_station_model_repr(domain_stations):
    station_mex = domain_stations[0]
    expected_result = '<Station> MEX'
    assert repr(station_mex) == expected_result


def test_station_model_comparison(domain_stations):
    station_mex = domain_stations[0]
    station_dict = {'code': 'MEX', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None}
    station = Station.from_dict(station_dict)
    assert station == station_mex


def test_station_is_singleton(domain_stations):
    station_mex = domain_stations[0]
    station_dict = {'code': 'MEX', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None}
    station = Station.from_dict(station_dict)
    assert station is station_mex
