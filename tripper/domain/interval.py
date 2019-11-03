from datetime import datetime, timedelta

from tripper.domain.duration import Duration


class Interval(object):
    """ An Interval represents a Duration occurring between a 'begin' and an 'end' datetime.

        begin and end datetimes should be timezone-aware. Although, python's duck typing feature
        allows for naive datetimes as well"""

    def __init__(self, begin: datetime, end: datetime):
        """Enter beginning and ending aware-datetime

        In order to facilitate object retrieval and storing, datetime objects are expected to be timezone-aware
        and in the UTC format
        """
        self._begin = begin
        self._end = end
        self._begin_timezone_displayed = None
        self._end_timezone_displayed = None

    @property
    def begin(self):
        """Will return begin as an aware datetime object set to begin_timezone"""
        if self._begin_timezone_displayed:
            return self._begin.astimezone(tz=self._begin_timezone_displayed)
        else:
            return self._begin

    @property
    def duration(self):
        return Duration.from_timedelta(td=self._end - self._begin)

    @property
    def end(self):
        if self._end_timezone_displayed:
            return self._end.astimezone(tz=self._end_timezone_displayed)
        else:
            return self._end

    @classmethod
    def from_timedelta(cls, begin: datetime, a_timedelta: timedelta):
        """Returns an Itinerary from a given begin datetime and the timedelta duration of it

        The created Itinerary's end field will have the same timezone as its begin field"""
        return cls(begin=begin, end=begin + a_timedelta)

    def astimezone(self, begin_timezone, end_timezone):
        """Changes the time zone to be displayed"""
        self._begin_timezone_displayed = begin_timezone
        self._end_timezone_displayed = end_timezone
