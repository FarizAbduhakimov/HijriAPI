import datetime

from rest_framework import serializers
from hijri_converter import Hijri, Gregorian


# class DateSerializer(serializers.Serializer):
#     dt = datetime.date.today()
#     hijri_day = Gregorian(dt.year, dt.month, dt.day).to_hijri()


