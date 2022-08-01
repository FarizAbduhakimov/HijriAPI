from django.shortcuts import render
from rest_framework.response import Response

from .serializers import DateSerializer


def list(request):
    serializer_class = DateSerializer()
    serialized_data = {'date': serializer_class.data}
    return Response(serialized_data)