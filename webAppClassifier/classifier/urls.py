from .views import *
from django.conf import settings
from django.urls import path
from .views import Index, ImageView, Display
from django.urls import path
urlpatterns = [
    path('', Index, name='index'),
    path('upload', ImageView, name='upload'),
    path('img/', Display, name='display')
]
