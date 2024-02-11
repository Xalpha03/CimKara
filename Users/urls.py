from django.urls import path
from .views import *
from django.contrib.auth import views


app_name = 'users'

urlpatterns = [
    path('login/', login_views, name="logIn"),
    path('logup/', logup_views, name='logup'),
    path('logout/', logout_views, name='logOut'),
    # path('logup/userCreate/', logup_user_create_views, name="createUser"),
    
    path('reset_password/', views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', views.PasswordResetDoneView.as_view(), name='reset_password_send'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='reset_password_confirm'),
    path('reset_password_complete/', views.PasswordResetCompleteView.as_view(), name='reset_password_complete'),
    
]
