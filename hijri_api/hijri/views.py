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

@api_view(['GET','POST'])
def to_hijri(request):
    year = request.data["year"]
    month = request.data["month"]
    day = request.data["day"]
    dt = datetime.datetime(year, month, day)
    
    # dt_value = "{year}-{month}-{day}".format(dt.year,
    #                                         dt.month,
    #                                         dt.day)
    hijri = Gregorian(dt.year, dt.month, dt.day).to_hijri()
    dict = {
            "year": hijri.year,
            "month": hijri.month,
            "day": hijri.day
        }
    
    return JsonResponse(dict)

