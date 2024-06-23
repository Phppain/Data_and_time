"""work2.py"""

import datetime

if __name__ == "__main__":
    YEAR = 2015
    WEEK_NUMBER = 50

    DATE = datetime.datetime.strptime(f'{YEAR} {WEEK_NUMBER} 1', '%G %V %u')
    print(f"пн {DATE.strftime('%d %B %H:%M:%S %Y')}")
