from django.urls import path
from .api import PredictionFeedbackApi, RegisterApi, FavoriteFlower
from .views import Index, ImageView, Display, thanks, contact, logoutView, loginView, favoriteView
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path("", Index, name="index"),
    path("upload", ImageView, name="upload"),
    path("img/", Display, name="display"),
    path("thanks", thanks, name="thank-you"),
    path("contact", contact, name="contact-us"),
    path("favorite", favoriteView, name="my-favorite"),

    path("api/register", RegisterApi.as_view()),
    path("api/favorite", FavoriteFlower.as_view()),
    path('logout', logoutView, name='logout'),
    path('login', loginView, name='login'),
    path("leave-feedback", PredictionFeedbackApi.as_view(), name="feedback-api"),
    path("api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
