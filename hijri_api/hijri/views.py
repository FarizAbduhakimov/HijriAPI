import datetime
from django.http import JsonResponse
from rest_framework.decorators import api_view
from hijri_converter import Hijri, Gregorian
from .months import hijri_months_dict, gregorian_months_dict
from .weekdays import hijri_days_dict, gregorian_days_dict



@api_view(['GET'])
def to_hijri(request):
    """Get Hijri date"""
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
    """Get gregorian date"""
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



@api_view(['GET'])
def hijri_months(request):
    """Hijri months"""
    return JsonResponse(hijri_months_dict())


@api_view(['GET'])
def gregorian_months(request):
    """Gregorian months"""
    return JsonResponse(gregorian_months_dict())


@api_view(['GET'])
def hijri_days(request):
    """Hijri weekdays"""
    return JsonResponse(hijri_days_dict())


@api_view(['GET'])
def gregorian_days(request):
    """Gregorian weekdays"""
    return JsonResponse(gregorian_days_dict())
