from django.urls import path
from masterchefapp.views import Home



urlpatterns = [
    path('',Home.as_view(), name ='home')
]
