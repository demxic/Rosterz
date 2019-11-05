import pytest

from tripper.request_objects import station_list_request_object as req


def test_build_station_list_request_object_without_parameters():
    request = req.StationListRequestObject()

    assert request.filters is None
    assert bool(request) is True


def test_build_station_list_request_object_from_empty_dict():
    request = req.StationListRequestObject.from_dict({})

    assert request.filters is None
    assert bool(request) is True


def test_build_station_list_request_object_with_empty_filters():
    request = req.StationListRequestObject(filters={})
    assert request.filters == {}
    assert bool(request) is True


def test_build_station_list_request_object_from_dict_with_empty_filters():
    request = req.StationListRequestObject.from_dict({'filters': {}})
    assert request.filters == {}
    assert bool(request) is True


def test_build_station_list_request_object_from_dict_with_filters_wrong():
    request = req.StationListRequestObject.from_dict({'filters': {'a': 1}})
    assert request.has_errors()
    assert request.errors[0]['parameter'] == 'filters'
    assert bool(request) is False


def test_build_station_list_request_object_from_dict_with_invalid_filters():
    request = req.StationListRequestObject.from_dict({'filters': 5})
    assert request.has_errors()
    assert request.errors[0]['parameter'] == 'filters'
    assert bool(request) is False


@pytest.mark.parametrize('key', ['continent__eq', 'tz_city__eq', 'codes_list'])
def test_build_station_list_request_object_accepted_filters(key):
    filters = {key: 'America'}
    request = req.StationListRequestObject.from_dict({'filters': filters})
    assert request.filters == filters
    assert bool(request) is True


@pytest.mark.parametrize('key', ['code__lt', 'code__gt'])
def test_build_station_list_request_object_rejected_filters(key):
    filters = {key: 1}
    request = req.StationListRequestObject.from_dict({'filters': filters})
    assert request.has_errors()
    assert request.errors[0]['parameter'] == 'filters'
    assert bool(request) is False
