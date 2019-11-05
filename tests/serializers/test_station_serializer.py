import json
import pytz

from tripper.domain.elements import Station
from tripper.serializers import station_json_serializer as ser


def test_serialize_domain_station():
    timezone = pytz.timezone('America/Mexico_City')
    station = Station(code='MEX', timezone=timezone, viaticum=None)
    expected_json = '{"__class__": "Station", "__args__": [], "__kw__": {"code": "MEX", "continent": ' \
                    '"America", "tz_city": "Mexico_City", "viaticum": null}} '
    json_station = json.dumps(station, cls=ser.StationJsonEncoder)
    assert json.loads(json_station) == json.loads(expected_json)
