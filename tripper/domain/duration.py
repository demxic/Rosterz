import re
from datetime import timedelta
from typing import Pattern


duration_fmt: Pattern[str] = re.compile(r"""
    (?P<fill_align>.?[<>])?            #4 digits for FLIGHT number
    (?P<size>\d)?     #3 letter destination IATA airport code             v.gr MEX, SCL, JFK
    (?P<colon>:)?             #4 digit begin time                                 v.gr.   0300, 1825
    (?P<hide_if_zero>H)?               #4 digit end time
    """, re.VERBOSE)


class Duration(object):
    """A duration is the equivalent of a datetime.timedelta with the added benefit of pretty printing

            It should be treated as a representation of minutes in an HH:MM format """
    default_format = '<4'

    def __init__(self, minutes: int):
        if minutes < 0:
            raise ValueError
        self.minutes = minutes

    @classmethod
    def from_timedelta(cls, td: timedelta):
        minutes = int(td.total_seconds() / 60)
        return cls(minutes)

    @classmethod
    def from_string(cls, duration_as_string):
        """Create a Duration from a string value which may or may not have a colon.
                123:30, 0:30, 1220, 0150 ---- all are valid duration representations
        """
        no_colon_string = duration_as_string.replace(':', '')
        hours, minutes = int(no_colon_string[0:-2]), int(no_colon_string[-2:])
        return cls(minutes=hours * 60 + minutes)

    def as_timedelta(self):
        return timedelta(minutes=self.minutes)

    def get_hours_and_minutes(self):
        """Returns the total number of hours and minutes in the duration as a tuple"""
        return divmod(self.minutes, 60)

    def __add__(self, other):
        if isinstance(other, Duration):
            return Duration(self.minutes + other.minutes)
        else:
            raise ValueError

    def __radd__(self, other):
        """Because sum(x) always starts adding a 0, Duration takes this into account in this method"""
        return Duration(self.minutes + other.minutes)

    def __sub__(self, other):
        return Duration(self.minutes - other.minutes)

    def __lt__(self, other):
        return self.minutes < other.minutes

    def __eq__(self, other):
        return self.minutes == other.minutes

    def __str__(self):
        """Prints as HHMM v.gr. 1230"""
        return self.__format__(Duration.default_format)

    def __repr__(self):
        return "{__class__.__name__}({minutes})".format(__class__=self.__class__, **self.__dict__)

    def __format__(self, format_spec):
        """Depending on format_spec value, a Duration can be printed as follow:

        [[fill]align][:][visibility]
        fill : character to be used to pad the field to the minimum width
        align : '<' - Forces the field to be left-aligned within the available space (This is the default.)
                '>' - Forces the field to be right-aligned within the available space.
        :       include the colon when it should be printed out
        visibility  :  Show or hide durations of 0 minutes.
                        " " - Show 00:00 or 0000 durations (This is the default.)
                        "H" - Show '    ' instead.
        """

        if format_spec == "":
            format_spec = self.default_format
        rs = duration_fmt.match(format_spec).groupdict()
        rs['fill_align'] = rs['fill_align'] if rs['fill_align'] else ''
        rs['size'] = rs['size'] if rs['size'] else ''
        rs['colon'] = rs['colon'] if rs['colon'] else ''
        if rs['hide_if_zero'] and self.minutes == 0:
            basic_string = ' '
        else:
            hours, minutes = self.get_hours_and_minutes()
            minutes = str(minutes) if minutes > 9 else '0' + str(minutes)
            hours = str(hours) if hours > 9 else '0' + str(hours)
            basic_string = "{0}{2}{1}".format(hours, minutes, rs['colon'])
        result = "{0:{fill_align}{size}s}".format(basic_string, **rs)
        return result
