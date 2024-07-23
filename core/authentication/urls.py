from django.urls import path
from .views import *

urlpatterns = [
    path('CompanyRegistration/', CompanyRegistration, name="CompanyRegistrationView"),
    path('login/', AuthLogin, name="AuthLoginView"),
]