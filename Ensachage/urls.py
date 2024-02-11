from django.urls import path
from .views import *
from django.http import HttpResponse
from django.contrib.auth.models import User



app_name = 'data'
urlpatterns = [
    path('', index_views, name="index_name"),
    path('detail/', detail_views, name="detail_name"),
    path('filter_by_year/', filter_views, name="filter_name"),
    path('yesterday/', yesterday_views, name="yesterday_name"),
    path('day/', day_views, name="day_name"),
    path('month/', month_views, name="month_name"),
    path('add_form/', add_form_views, name='add_form_name'),
    path('update/', update_form_views, name="update_name"),
]