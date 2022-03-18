from django.contrib import admin

from .models import Prediction, Result, FavoritePrediction

admin.site.register(Prediction)
admin.site.register(Result)
admin.site.register(FavoritePrediction)
