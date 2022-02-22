from .views import *
from django.urls import path, include
from django.shortcuts import render

urlpatterns = [
    path('index', Home),
]