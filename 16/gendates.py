from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    start = 0
    while True:
        start += 1
        if start %  100 == 0 or start % 365 == 0:
            yield PYBITES_BORN + timedelta(days=start)
            