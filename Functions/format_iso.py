# The get_str_date(date) function converts the date from the database into ISO format.

from datetime import datetime


def get_str_date(date):
    
    dt = date.split()[0]
    d = datetime.strptime(dt, "%Y-%m-%d")
    return datetime.strftime(d, "%A %d %B %Y")


if __name__ == "__main__":
    print(get_str_date('2021-05-27 17:08:34.149Z'))
