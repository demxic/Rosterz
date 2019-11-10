import pytz
from tripper.domain.elements import Route


def test_route_model_init(domain_stations):
    mex = domain_stations[0]
    route = Route(name='T1', origin=mex, destination=mex, id=1)
    assert route.name == 'T1'
    assert route.origin == mex
    assert route.destination == mex
    assert route.id == 1


def test_route_model_from_dict(route_dicts):
    route_dict = route_dicts[0]
    route = Route.from_dict(route_dict)
    assert route.name == route_dict['name']
    assert route.origin.to_dict() == route_dict['origin']
    assert route.destination.to_dict() == route_dict['destination']
    assert route.id == route_dict['id']


def test_route_model_to_dict(route_dicts):
    route_dict = route_dicts[0]
    route = Route.from_dict(route_dict)
    assert route.to_dict() == route_dict


def test_route_model_str(domain_routes):
    route_001 = domain_routes[0]
    expected_result = 'T1 MEX MEX'
    assert str(route_001) == expected_result


def test_route_model_repr(domain_routes):
    route_001 = domain_routes[0]
    expected_result = '<Route> T1 MEX MEX'
    assert repr(route_001) == expected_result


def test_route_model_comparison(route_dicts, domain_routes):
    route_dict = route_dicts[0]
    route = Route.from_dict(route_dict)
    assert route == domain_routes[0]


def test_route_is_singleton(route_dicts, domain_routes):
    route_dict = route_dicts[0]
    route_0001 = domain_routes[0]
    assert Route.from_dict(route_dict) is route_0001
