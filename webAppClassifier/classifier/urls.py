from .views import *
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', Index, name='index'),
    path('upload', ImageView, name='upload'),
    path('img/', Display, name='display')
]
