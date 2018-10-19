from random import randrange
from string import ascii_lowercase
import datetime
import random


def random_url(size=5):
    url = ''.join(random.choice(ascii_lowercase) for i in range(12))
    return ('.'.join(["www", url, "com.au"]))


def random_date(start, limit):
    current = start
    while limit >= 0:
        curr = current + datetime.timedelta(minutes=randrange(60))
        yield curr
        limit -= 1


def random_ip():
    return (".".join(map(str, (random.randint(0, 255) for _ in range(4)))))


def random_data(start_date):
    for x in random_date(start_date, 10):
        string = ",".join(
            [str(datetime.datetime.now().strftime("%d/%m/%y %H:%M")), x.strftime("%d/%m/%y %H:%M"), random_ip(),
             random_url(4)])
        print(string)


while True:
    for year in range(2016, 2050):
        month = 10
        for day in range(1, 30):
            start_date = datetime.datetime(year, month, day, 13, 00)
            random_data(start_date)
