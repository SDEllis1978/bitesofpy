import calendar
import datetime

def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    dob = calendar.weekday(date.year, date.month, date.day)
    return calendar.day_name[dob]

