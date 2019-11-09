import json
from typing import List
from unittest import mock

from tripper.domain.elements import Station
from tripper.response_objects import response_objects as res

station_dict = {
    'code': 'MEX',
    'continent': 'America',
    'tz_city': 'Mexico_City',
    'viaticum': None
}

station = Station.from_dict(a_dict=station_dict)

stations: List[Station] = [station]


@mock.patch('tripper.use_cases.station_list_use_case.StationListUseCase')
def test_get(mock_use_case, client):
    """Client: is one of the fixtures provided by pytest-flask; it automatically loads the app,
        which we defined in conftest.py, and is an object that simulates an HTTP client that can access
        the API endpoints and store the responses of the server."""
    mock_use_case().execute.return_value = res.ResponseSuccess(value=stations)

    http_response = client.get('/rooms')

    assert json.loads(http_response.data.decode('UTF-8')) == [station_dict]

    # "Execute" is run on an instance of the RoomListUseCase class, and not on the class itself,
    #        which is why we call the mock (mock_use_case()) before accessing the method."""
    mock_use_case().execute.assert_called()
    args, kwargs = mock_use_case().execute.call_args
    assert args[0].filters == {}
    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'


@mock.patch('tripper.use_cases.station_list_use_case.StationListUseCase')
def test_get_with_filters(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess(stations)

    http_response = client.get('/stations?filter_continent__eq=America')

    assert json.loads(http_response.data.decode) == [station_dict]

    mock_use_case().execute.assert_called()
    args, kwargs = mock_use_case().execute.call_args
    assert args[0].filters == {'continent__eq': 'America'}

    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'
