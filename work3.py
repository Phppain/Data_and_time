"""work3.py"""

import datetime

if __name__ == "__main__":
    YEAR = int(input("Enter an year: "))
    start_date = datetime.date(YEAR, 1, 1)
    end_date = datetime.date(YEAR, 12, 31)
    sundays = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() == 6: 
            sundays.append(current_date)
        current_date += datetime.timedelta(days=1)
    for sunday in sundays:
        print(sunday.strftime('%d %B %Y'))
