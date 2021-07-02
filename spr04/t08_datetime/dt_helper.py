from datetime import datetime
import pytz

def create_datetime(*args, timezone_str=None):
    if timezone_str:
        timezone = pytz.timezone(timezone_str)
        date = datetime(args[0], args[1], args[2], args[3], args[4], tzinfo=timezone)
    else:
        date = datetime(args[0], args[1], args[2], args[3], args[4])
    print(date)
    return date


def print_formatted_datetime(datetime, format):
    print(datetime.strftime(format))

def print_difference(datetime1, datetime2, timezone_str = None):
    if timezone_str:
        timezone = pytz.timezone(timezone_str)
        datetime1.replace(tzinfo=timezone).astimezone(tz=None)
        datetime2.replace(tzinfo=timezone).astimezone(tz=None)
    print(datetime1 - datetime2)