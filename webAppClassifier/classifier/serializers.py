"""
from .models import Prediction
from django.db import models


class PredictionSerializer(serializers.ModelSerializer):
    image = models.ImageField(upload_to="img/%Y/%m/%d/", blank=False)

    class Meta:
        model = Prediction
        fields = "image"
"""
