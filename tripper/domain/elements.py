import pytz


class Station(object):
    """ Create airports using the Flyweight pattern
    Try using the weakref.WeakValueDictionary() if  garbage-collection concerned
    for our simple app, not needed
    """
    _stations = dict()

    def __new__(cls, code: str, timezone, viaticum):
        station = cls._stations.get(code)
        if not station:
            station = super().__new__(cls)
            if timezone:
                cls._stations[code] = station
        return station

    def __init__(self, code: str, timezone, viaticum=None):
        self.code = code
        self.timezone = timezone
        self.continent, self.tz_city = timezone.zone.split('/')
        self.viaticum = viaticum

    @classmethod
    def from_dict(cls, a_dict):
        return cls(code=a_dict['code'],
                   timezone=pytz.timezone(a_dict['continent'] + '/' + a_dict['tz_city']),
                   viaticum=a_dict['viaticum'])

    def to_dict(self):
        return dict(code=self.code, continent=self.continent, tz_city=self.tz_city, viaticum=self.viaticum)

    def __eq__(self, other: 'Station'):
        return self.to_dict == other.to_dict

    def __str__(self):
        return "{}".format(self.code)

    def __repr__(self):
        return "<Station> {}".format(self.code)
