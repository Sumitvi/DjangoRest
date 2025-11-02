from django.contrib import admin
from django.urls import path , include
from .views import *;
from .views import PersonViewSet , RegisterView , PersonAPI
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('person', PersonViewSet)

urlpatterns = [
    
    path('', include(router.urls)),

    # path('login/', login , name='Login View' ),
    path('person/', person , name='Person' ),
    path('auth/' , Auth , name="Auth"),
    path('person-api/' , PersonAPI.as_view()),
    path('register/' , RegisterView.as_view() ),
    path('login/' , LoginView.as_view())

]