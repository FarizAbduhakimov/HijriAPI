import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from hijri_converter import Gregorian
from rest_framework.response import Response




def date(request):
    dt = datetime.date.today()
    hijri_day = Gregorian(dt.year, dt.month, dt.day).to_hijri()
    # hijri_data = {'date': hijri_day}
    return HttpResponse(hijri_day)