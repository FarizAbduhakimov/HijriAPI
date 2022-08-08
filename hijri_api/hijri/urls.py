from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("tohijri/", views.to_hijri),
    path("togregorian/", views.to_gregorian),
    path("months/hijri", views.hijri_months),
    path("months/gregorian", views.gregorian_months),
    path("weekdays/hijri", views.hijri_days),
    path("weekdays/gregorian", views.gregorian_days)
]