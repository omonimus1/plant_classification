from .views import IndexView, ImageView, Display, thanks
from django.urls import path
from .views import GetPredictionApi

urlpatterns = [
    path("", IndexView, name="index"),
    path("upload", ImageView, name="upload"),
    path("img/", Display, name="display"),
    path('thanks', thanks, name='thank-you'),
    # mobile APIs
    path("getPrediction", GetPredictionApi.as_view(), name="Prediction APIs"),
]
