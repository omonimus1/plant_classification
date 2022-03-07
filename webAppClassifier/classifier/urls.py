from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .api import PredictionFeedbackApi, PredictionAPI
from .views import Index, ImageView, Display, thanks

urlpatterns = [
    path("", Index, name="index"),
    path("upload", ImageView, name="upload"),
    path("img/", Display, name="display"),
    path("thanks", thanks, name="thank-you"),
    path('leave-feedback', PredictionFeedbackApi.as_view(), name='feedback-api'),
    path('get-prediction', PredictionAPI.as_view(), name='get-prediction')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # imp for what you want to achieve.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
