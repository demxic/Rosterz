from tripper.repository import memrepo as mr
from tripper.use_cases import station_list_use_case as uc
from tripper.request_objects import station_list_request_object as req

airport_data = [
    {'code': 'station_mex', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None},
    {'code': 'GDL', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None},
    {'code': 'JFK', 'continent': 'America', 'tz_city': 'New_York', 'viaticum': None},
    {'code': 'MAD', 'continent': 'Europe', 'tz_city': 'Madrid', 'viaticum': None}
]

repo = mr.MemRepo(airport_data)
use_case = uc.StationListUseCase(repo=repo)
request_object = req.StationListRequestObject.from_dict(adict={'filters': {'continent__eq': 'America'}})
response = use_case.execute(request_object=request_object)
print(response.value)
