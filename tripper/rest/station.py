import json

from flask import Blueprint, Response, request

from tripper.repository import memrepo as mr
from tripper.use_cases import station_list_use_case as uc
from tripper.serializers import station_json_serializer as ser
from tripper.request_objects import station_list_request_object as req
from tripper.response_objects import response_objects as res

blueprint = Blueprint('station', __name__)

STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500
}

station1 = {'code': 'MEX', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None}
station2 = {'code': 'GDL', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None}
station3 = {'code': 'JFK', 'continent': 'America', 'tz_city': 'New_York', 'viaticum': None}
station4 = {'code': 'MAD', 'continent': 'Europe', 'tz_city': 'Madrid', 'viaticum': None}


@blueprint.route('/stations', methods=['GET'])
def station():
    qrystr_params = {
            'filters': {},
        }

    for arg, values in request.args.items():
        if arg.startswith('filter_'):
            qrystr_params['filters'][arg.replace('filter_', '')] = values
    request_object = req.StationListRequestObject.from_dict(qrystr_params)
    repo = mr.MemRepo([station1, station2, station3])
    use_case = uc.StationListUseCase(repo)
    response = use_case.execute(request_object)
    return Response(json.dumps(response.value, cls=ser.StationJsonEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])
