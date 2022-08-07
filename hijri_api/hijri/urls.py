from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("tohijri/", views.to_hijri),
    path("togregorian/", views.to_gregorian)
]