from django.contrib import admin
from django.urls import path
from .views import *;

urlpatterns = [
    path('login/', login , name='Login View' ),
    path('person/', person , name='Person' ),
    path('auth/' , Auth , name="Auth"),
    path('person-api/' , PersonAPI.as_view())

]