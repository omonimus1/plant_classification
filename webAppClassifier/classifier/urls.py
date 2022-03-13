from django.urls import path

from .api import PredictionFeedbackApi, RegisterApi, FavoriteFlower
from .views import Index, ImageView, Display, thanks, contact, logout
from django.conf import settings

urlpatterns = [
    path("", Index, name="index"),
    path("upload", ImageView, name="upload"),
    path("img/", Display, name="display"),
    path("thanks", thanks, name="thank-you"),
    path("contact", contact, name="contact-us"),
    path("api/register", RegisterApi.as_view()),
    path("api/favorite", FavoriteFlower.as_view()),
    path('logout', logout, name='logout'),
    path("leave-feedback", PredictionFeedbackApi.as_view(), name="feedback-api"),
]
