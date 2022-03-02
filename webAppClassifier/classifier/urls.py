from .views import IndexView, ImageView, Display
from django.urls import path

urlpatterns = [
    path("", IndexView, name="index"),
    path("upload", ImageView, name="upload"),
    path("img/", Display, name="display"),
]
