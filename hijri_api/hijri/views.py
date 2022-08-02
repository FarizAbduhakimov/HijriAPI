import datetime
from django.http import JsonResponse
from django.shortcuts import render

from hijri_converter import Gregorian
from rest_framework.response import Response



# def date(request):
#     dt = datetime.date.today()
#     serialized_data = {'date': dt}
#     return JsonResponse(serialized_data)



def date(request):
    dt = datetime.date.today()
    hijri_day = Gregorian(dt.year, dt.month, dt.day).to_hijri()
    hijri_data = {'date': hijri_day}
    return JsonResponse(hijri_data)