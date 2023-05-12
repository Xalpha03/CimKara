from django.urls import path
from .views import *

app_name = 'product'
urlpatterns = [
    path('', index_view, name='index'),
    path('details/', detail_view, name='details'),
    path('edite/', edite_view, name='edite'),
]