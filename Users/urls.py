from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    path('login/', loginView, name='login'),
    path('logup/', logupView, name='logup'),
    path('logout/', logoutView, name='logout'),
]