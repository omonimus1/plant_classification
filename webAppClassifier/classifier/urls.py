from django.urls import path

from .api import PredictionFeedbackApi, RegisterApi
from .views import Index, ImageView, Display, thanks

urlpatterns = [
    path("", Index, name="index"),
    path("upload", ImageView, name="upload"),
    path("img/", Display, name="display"),
    path("thanks", thanks, name="thank-you"),
    path('api/register', RegisterApi.as_view()),
    path('leave-feedback', PredictionFeedbackApi.as_view(), name='feedback-api')
]
