import pytz
from tripper.domain.elements import Station


def test_station_model_init():
    a = Station(code='MEX', timezone=pytz.timezone('America/Mexico_City'), viaticum=None)
    assert a.code == 'MEX'
    assert a.continent == 'America'
    assert a.tz_city == 'Mexico_City'
    assert a.viaticum is None
    assert a.timezone == pytz.timezone('America/Mexico_City')


def test_station_model_from_dict():
    station_dict = {'code': 'MEX', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None}
    a = Station.from_dict(station_dict)
    assert a.code == 'MEX'
    assert a.continent == 'America'
    assert a.tz_city == 'Mexico_City'
    assert a.viaticum is None
    assert a.timezone == pytz.timezone('America/Mexico_City')


def test_station_model_to_dict():
    station_dict = {'code': 'MEX', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None}
    a = Station.from_dict(station_dict)
    assert a.to_dict()


def test_station_model_str():
    station_dict = {'code': 'MEX', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None}
    a = Station.from_dict(station_dict)
    expected_result = 'MEX'
    assert str(a) == expected_result


def test_station_model_repr():
    station_dict = {'code': 'MEX', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None}
    a = Station.from_dict(station_dict)
    expected_result = '<Station> MEX'
    assert repr(a) == expected_result


def test_station_model_comparison():
    station_dict = {'code': 'MEX', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None}
    station1 = Station.from_dict(station_dict)
    station2 = Station.from_dict(station_dict)
    assert station1 == station2
