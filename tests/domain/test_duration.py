import datetime

import pytest

from tripper.domain.duration import Duration


def test_duration_init():
    duration = Duration(minutes=300)
    assert duration.minutes == 300


def test_duration_with_negative_number():
    with pytest.raises(ValueError):
        Duration(minutes=-300)


def test_duration_from_a_timedelta():
    minutes = 30
    td = datetime.timedelta(minutes=minutes)
    duration = Duration.from_timedelta(td=td)
    assert duration.minutes == minutes


def test_duration_from_string_with_colon():
    duration_as_string = '23:40'
    duration = Duration.from_string(duration_as_string)
    assert duration.minutes == 23*60 + 40


def test_duration_from_string_without_colon():
    duration_as_string = '2340'
    duration = Duration.from_string(duration_as_string)
    assert duration.minutes == 23*60 + 40


def test_duration_as_a_timedelta():
    minutes = 320
    duration = Duration(minutes=minutes)
    td = duration.as_timedelta()
    assert isinstance(td, datetime.timedelta)
    assert minutes == td.total_seconds() / 60


def test_get_hour_and_minutes():
    hours = 25
    minutes = 42
    duration = Duration(minutes=hours * 60 + minutes)
    result = duration.get_hours_and_minutes()
    assert hours, minutes == result


def test_add_two_durations():
    d1 = Duration(minutes=6*60+23)
    d2 = Duration(minutes=3*60+45)
    d3 = d1 + d2
    assert d3.minutes == (6*60+23) + (3*60+45)


def test_add_duration_to_a_number():
    d1 = Duration(minutes=40)
    d2 = 0
    with pytest.raises(ValueError):
        d1 + d2


def test_larger_duration_minus_smaller():
    d1 = Duration(minutes=320)
    d2 = Duration(minutes=100)
    assert 220 == (d1-d2).minutes


def test_smaller_duration_minus_larger():
    d1 = Duration(minutes=320)
    d2 = Duration(minutes=100)
    with pytest.raises(ValueError):
        d2 - d1


def test_comparisons_between_durations():
    d1 = Duration(minutes=320)
    d2 = Duration(minutes=100)
    assert d2 < d1
    assert d2 != d1
    assert d2 == d2
    assert d1 == d1


def test_string_representation():
    assert str(Duration(minutes=4 * 60 + 30)) == '0430'


def test_format_show_zeros_no_colon():
    d1 = Duration(minutes=0)
    expected_result = '0000'
    assert d1.__format__('') == expected_result


def test_format_show_zeros_with_colon():
    d1 = Duration(minutes=0)
    expected_result = '00:00'
    assert d1.__format__(':') == expected_result


def test_format_not_show_when_duration_is_zero():
    d1 = Duration(minutes=0)
    expected_result = ' '
    assert d1.__format__('0<H') == expected_result


def test_format_five_digits_with_colon():
    d1 = Duration(minutes=123*60 + 40)
    expected_result = '123:40'
    assert d1.__format__(':') == expected_result


def test_format_four_digits_with_colon():
    d1 = Duration(minutes=20*60 + 30)
    expected_result = '20:30'
    assert d1.__format__('0<4:') == expected_result


def test_format_four_digits_without_colon():
    d1 = Duration(minutes=20*60 + 30)
    expected_result = '2030'
    assert d1.__format__('0<4') == expected_result

