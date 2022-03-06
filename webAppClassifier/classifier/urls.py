<<<<<<< HEAD
from django.urls import path
from .views import Index, ImageView, Display, thanks
=======
from .views import Index, ImageView, Display
from django.urls import path
>>>>>>> dev

urlpatterns = [
    path("", Index, name="index"),
    path("upload", ImageView, name="upload"),
    path("img/", Display, name="display"),
<<<<<<< HEAD
    path("thanks", thanks, name="thank-you"),
=======
>>>>>>> dev
]
