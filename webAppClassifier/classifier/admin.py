from django.contrib import admin

from .models import Prediction, Result, Favorite

admin.site.register(Prediction)
admin.site.register(Result)
admin.site.register(Favorite)
