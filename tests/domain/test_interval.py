import pytz
from datetime import datetime

from tripper.domain.interval import Interval
from tripper.domain.duration import Duration


def test_interval_init(interval_dicts):
    begin = pytz.utc.localize(datetime(**interval_dicts[0][0]))
    end = pytz.utc.localize(datetime(**interval_dicts[0][1]))
    interval = Interval(begin=begin, end=end)
    assert interval._begin == begin
    assert interval._end == end
    assert interval._begin_timezone_displayed is None
    assert interval._end_timezone_displayed is None


def test_interval_as_timezone(domain_intervals):
    interval = domain_intervals[0]
    interval.astimezone(begin_timezone=pytz.timezone('America/New_York'),
                        end_timezone=pytz.timezone('America/Mexico_City'))
    assert interval.begin.tzinfo.zone == 'America/New_York'
    assert interval.end.tzinfo.zone == 'America/Mexico_City'


def test_interval_duration(domain_intervals):
    interval = domain_intervals[0]
    assert interval.duration == Duration.from_timedelta(interval._end - interval._begin)


def test_interval_from_timedelta(domain_intervals):
    interval = domain_intervals[0]
    td = interval._end - interval._begin
    i = Interval.from_timedelta(begin=interval._begin, a_timedelta=td)
    assert i.begin == interval.begin
    assert i.end == interval.end
    assert i.duration.as_timedelta() == td
    assert isinstance(i, Interval)
