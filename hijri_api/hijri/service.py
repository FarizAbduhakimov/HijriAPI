import datetime

from hijri_converter import Hijri, Gregorian

def get_day(*args, **kwargs):
    greg_day = datetime.date.today().strftime("%Y%m%d")
    hijri_day = Gregorian(int(greg_day)).to_hijri()
    hijri_day.strftime("%Y%m%d")

    return hijri_day

get_day()