from .views import IndexView, ImageView, Display, thanks
from django.urls import path
from .apis import GetPredictionApi, PredictionFeedbackApi

urlpatterns = [
    path("", IndexView, name="index"),
    path("upload", ImageView, name="upload"),
    path("img/", Display, name="display"),
    path('thanks', thanks, name='thank-you'),
    path('prediction-feedback', PredictionFeedbackApi.as_view()),
    # mobile APIs
    path("getPrediction", GetPredictionApi.as_view(), name="Prediction APIs"),
]
