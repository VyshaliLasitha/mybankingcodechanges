from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', index,name='home' ),
    path('login/' , loginpage, name = 'loginpage'),
    path('logout/', logoutUser, name='logout'),
]
