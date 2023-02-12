# The function determines the number of days in a specific month.

from datetime import date


def get_days_in_month(month, year):
    if month < 12:
        difference = date(year, month + 1, 1) - date(year, month, 1)
        return difference.days
    else:
        return 31


if __name__ == "__main__":
    print(get_days_in_month(2, 2020))
