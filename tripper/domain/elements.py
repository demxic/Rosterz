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
        self.viaticum = viaticum

    @classmethod
    def from_dict(cls, a_dict):
        return cls(code=a_dict['code'],
                   timezone=a_dict['timezone'],
                   viaticum=a_dict['viaticum'])

    def to_dict(self):
        return dict(code=self.code, timezone=self.timezone, viaticum=self.viaticum)

    def __eq__(self, other: 'Station'):
        return self.to_dict == other.to_dict

    def __str__(self):
        return "{}".format(self.code)

    def __repr__(self):
        return "<Station> {}".format(self.code)


class Route(object):
    """For a given airline, represents a flight number or ground duty name
        with its origin and destination airports
        Note: flights and ground duties are called Events"""
    _routes = dict()

    def __new__(cls, name: str, origin: Station, destination: Station, id: int = None):
        route_key = name + origin.code + destination.code
        route = cls._routes.get(route_key)
        if not route:
            route = super().__new__(cls)
            if id:
                cls._routes[route_key] = route
        return route

    def __init__(self, name: str, origin: Station, destination: Station, id: int = None):
        """Flight numbers have 4 digits only"""
        if not hasattr(self, 'initted'):
            self.id = id
            self.name = name
            self.origin = origin
            self.destination = destination
            self.initted = True

    @classmethod
    def from_dict(cls, a_dict):
        return cls(name=a_dict['name'],
                   origin=Station.from_dict(a_dict=a_dict['origin']),
                   destination=Station.from_dict(a_dict=a_dict['destination']),
                   id=a_dict['id'])

    def to_dict(self):
        return dict(id=self.id, name=self.name, origin=self.origin.to_dict(),
                    destination=self.destination.to_dict())

    def __eq__(self, other):
        """Two routes are the same if their parameters are equal"""
        return self.to_dict() == other.to_dict()

    def __str__(self):
        return "{name} {origin} {destination}".format(**self.__dict__)

    def __repr__(self):
        return "<{__class__.__name__}> {name} {origin} {destination}".format(
            __class__=self.__class__, **self.__dict__)
