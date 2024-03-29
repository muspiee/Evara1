from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('reg_user/', reg_user, name='reg_user'),
    path('login_user/', login_user, name='login_user'),
    path('user_auth/', user_auth ,name='user_auth'),
    path('otp_verify/', otp_verify ,name='otp_verify'),
    path('user_logout/', user_logout ,name='user_logout'),
    path('reset/', reset ,name='reset'),
    path('otp_reset/', otp_reset ,name='otp_reset'),
    path('dashboard/', dashboard ,name='dashboard'),
]

