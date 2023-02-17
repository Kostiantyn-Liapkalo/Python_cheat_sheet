

# The get_days_from_today(date) function returns the number of days from the current date.
from datetime import datetime


def get_days_from_today(date):
    y, m, d = map(int, date.split("-"))
    difference = datetime.now().date() - datetime(year=y, month=m, day=d).date()
    return difference.days


if __name__ == "__main__":
    print(get_days_from_today('2022-10-09'))