import datetime
from django.http import JsonResponse
from rest_framework.decorators import api_view
from hijri_converter import Hijri, Gregorian




@api_view(['GET'])
def to_hijri(request):
    year = request.data["year"]
    month = request.data["month"]
    day = request.data["day"]
    dt = datetime.datetime(year, month, day)
    hijri = Gregorian(dt.year, dt.month, dt.day).to_hijri()
    hijri_date = {
            "year": hijri.year,
            "month": hijri.month,
            "day": hijri.day
        }
    
    return JsonResponse(hijri_date)


@api_view(['GET'])
def to_gregorian(request):
    """Get hijri date"""
    year = request.data["year"]
    month = request.data["month"]
    day = request.data["day"]
    dt = datetime.datetime(year, month, day)
    gregorian = Hijri(dt.year, dt.month, dt.day).to_gregorian()

    gregorian_date = {
            "year": gregorian.year,
            "month": gregorian.month,
            "day": gregorian.day
        }
    
    return JsonResponse(gregorian_date)
