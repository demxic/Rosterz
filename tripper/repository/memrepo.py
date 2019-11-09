from tripper.domain.elements import Station


class MemRepo(object):

    def __init__(self, data):
        self.data = data

    def list(self, filters: dict = None):
        result = [Station.from_dict(a) for a in self.data]

        if filters is None:
            return result
        if 'continent__eq' in filters:
            result = [station for station in result if station.continent == filters['continent__eq']]
        if 'codes_list' in filters:
            result = [station for station in result if station.code in filters['codes_list']]
        if 'tz_city__eq' in filters:
            result = [station for station in result if station.tz_city in filters['tz_city__eq']]

        return result
