from datetime import datetime, timedelta

def add_gigasecond(birth_date):
    giga = timedelta(seconds = 1000000000)
    birth_date += giga
    return birth_date

print(add_gigasecond(datetime(2011, 4, 25)))
print(type(add_gigasecond(datetime(1977, 6, 13))))
