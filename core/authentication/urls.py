from django.urls import path
from .views import *

urlpatterns = [
    path('login/', user_login, name="UserLoginView"),
    path('request_otp/', request_otp, name="RequestOTP"),
]