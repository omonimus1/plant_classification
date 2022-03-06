from django.urls import path
from .views import Index, ImageView, Display, thanks

urlpatterns = [
    path("", Index, name="index"),
    path("upload", ImageView, name="upload"),
    path("img/", Display, name="display"),
    path("thanks", thanks, name="thank-you"),
]
