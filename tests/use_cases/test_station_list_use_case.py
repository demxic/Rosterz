# ------------- Version two with response and request objects:
import pytest
from unittest import mock

import pytz

from tripper.domain.elements import Station
from tripper.use_cases import station_list_use_case as uc
from tripper.request_objects import station_list_request_object as req
from tripper.response_objects import response_objects as res


@pytest.fixture
def domain_stations():
    station1 = Station(code='MEX', timezone=pytz.timezone('America/Mexico_City'))
    station2 = Station(code='GDL', timezone=pytz.timezone('America/Mexico_City'))
    station3 = Station(code='JFK', timezone=pytz.timezone('America/New_York'))
    station4 = Station(code='MAD', timezone=pytz.timezone('Europe/Madrid'))
    return [station1, station2, station3, station4]


def test_station_list_without_parameters(domain_stations):
    repository = mock.Mock()
    repository.list.return_value = domain_stations

    station_list_use_case = uc.StationListUseCase(repository)
    request = req.StationListRequestObject()

    response = station_list_use_case.execute(request)

    assert bool(response) is True
    repository.list.assert_called_with(filters=None)
    assert response.value == domain_stations


def test_station_with_filters(domain_stations):
    repository = mock.Mock()
    repository.list.return_value = domain_stations

    station_list_use_case = uc.StationListUseCase(repo=repository)
    qry_filter = {'continent__eq': 'all'}
    request_object = req.StationListRequestObject.from_dict({'filters': qry_filter})

    response_object = station_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repository.list.assert_called_with(filters=qry_filter)
    assert response_object.value == domain_stations


def test_station_list_handles_generic_error(domain_stations):
    repo = mock.Mock()
    repo.list.side_effect = Exception('Just an error message')

    station_list_use_case = uc.StationListUseCase(repo)
    request_object = req.StationListRequestObject.from_dict({})

    response_object = station_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {'type': res.ResponseFailure.SYSTEM_ERROR,
                                     'message': 'Exception: Just an error message'}


def test_station_list_handles_bad_request(domain_stations):
    repo = mock.Mock()

    station_list_use_case = uc.StationListUseCase(repo=repo)
    request_object = req.StationListRequestObject.from_dict({'filters': 5})

    response_object = station_list_use_case.execute(request_object=request_object)

    assert bool(response_object) is False
    assert response_object.value == {'type': res.ResponseFailure.PARAMETERS_ERROR,
                                     'message': 'filters: Is not iterable'}