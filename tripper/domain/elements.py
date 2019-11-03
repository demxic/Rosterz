import pytz


class Station(object):
    """Defines an airport operated by an airline"""

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
        return dict(iata_code=self.code, zone=self.timezone, viaticum=self.viaticum)

    def __eq__(self, other: 'Station'):
        return self.to_dict() == other.to_dict()

    def __str__(self):
        return "{}".format(self.code)

    def __repr__(self):
        return "<Station> {}".format(self.code)
