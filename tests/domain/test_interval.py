from datetime import datetime

import pytest
import pytz

from tripper.domain.interval import Interval
from tripper.domain.duration import Duration


@pytest.fixture
def domain_intervals():
    class A(object):

        def __init__(self):
            self.begin = pytz.utc.localize(datetime(year=2019, month=9, day=22, hour=16, minute=30))
            self.end = pytz.utc.localize(datetime(year=2019, month=9, day=22, hour=18, minute=45))
            self.i = Interval(begin=self.begin, end=self.end)
    return A()


def test_interval_init(domain_intervals):
    assert domain_intervals.i._begin == domain_intervals.begin
    assert domain_intervals.i._end == domain_intervals.end
    assert domain_intervals.i._begin_timezone_displayed is None
    assert domain_intervals.i._end_timezone_displayed is None


def test_interval_as_timezone(domain_intervals):
    domain_intervals.i.astimezone(begin_timezone=pytz.timezone('America/New_York'),
                                  end_timezone=pytz.timezone('America/Mexico_City'))
    assert domain_intervals.i.begin.tzinfo.zone == 'America/New_York'
    assert domain_intervals.i.end.tzinfo.zone == 'America/Mexico_City'


def test_interval_duration(domain_intervals):
    assert domain_intervals.i.duration == Duration(minutes=2 * 60 + 15)


def test_interval_from_timedelta(domain_intervals):
    td = domain_intervals.end - domain_intervals.begin
    i = Interval.from_timedelta(begin=domain_intervals.begin, a_timedelta=td)
    assert i.begin == domain_intervals.begin
    assert i.end == domain_intervals.end
    assert i.duration.as_timedelta() == td
    assert isinstance(i, Interval)
