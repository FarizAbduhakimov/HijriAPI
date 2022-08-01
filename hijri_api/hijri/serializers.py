import datetime

from rest_framework import serializers
from hijri_converter import Hijri, Gregorian


class DateSerializer(serializers.Serializer):
    greg_day = serializers.DateField(initial=datetime.date.today)
    hijri_day = Gregorian(greg_day).to_hijri()
    hijri_day.strftime("%Y %m %d")


