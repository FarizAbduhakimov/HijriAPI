import datetime
from hijri_converter import Hijri, Gregorian


def get_hijri_day(*args, **kwargs):
    dt = datetime.date.today()
    hijri_day = Gregorian(dt.year, dt.month, dt.day).to_hijri()

    print(hijri_day)

