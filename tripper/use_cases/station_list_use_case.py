from tripper.request_objects.station_list_request_object import StationListRequestObject
from tripper.response_objects import response_objects as res


class StationListUseCase(object):

    def __init__(self, repo):
        self.repo = repo

    def execute(self, request_object: StationListRequestObject):
        if not request_object:
            return res.ResponseFailure.build_from_invalid_request_object(request_object)
        try:
            stations = self.repo.list(filters=request_object.filters)
            return res.ResponseSuccess(stations)
        except Exception as exc:
            return res.ResponseFailure.build_system_error("{}: {}".format(exc.__class__.__name__, "{}".format(exc)))


