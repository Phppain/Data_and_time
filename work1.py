"""work1.py"""

import datetime

if __name__ == "__main__":

    DATE = datetime.datetime.strptime(input(), "%Y-%m-%d").date()

    print(DATE.isocalendar()[1])
