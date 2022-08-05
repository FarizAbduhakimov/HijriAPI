import datetime
from django.http import HttpResponse, JsonResponse
from dateutil.parser import parse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from hijri_converter import Gregorian
from rest_framework.response import Response




# def date(request):
#     dt = datetime.date.today()
#     hijri_day = Gregorian(dt.year, dt.month, dt.day).to_hijri()
#     # hijri_data = {'date': hijri_day}
#     return HttpResponse(hijri_day)

@api_view(['POST',])
def to_hijri(request):
    date = request.data["year", "month", "day"]
    h = Gregorian(date.year, date.month, date.day).to_hijri()
    dt_value = "{year}-{month}-{day}".format(date.year,
                                            date.month,
                                            date.day)
    # dict = {
    #         "date": h
    #     }
    
    return JsonResponse(datetime.strptime(h, '%Y-%m-%d'))

