"""work4.py"""

import datetime

def add_years(dt, years):
    """This func add years for any date"""
    try:
        new_date = dt.replace(year=dt.year + years)
    except ValueError:
        if dt.month == 2 and dt.day == 29:
            new_date = dt.replace(year=dt.year + years, day=28)
        else:
            raise
    return new_date

if __name__ == "__main__":
    print (add_years (datetime.date (2015,1,1), -1))
    print (add_years (datetime.date (2015,1,1), 0))
    print (add_years (datetime.date (2015,1,1), 2))
