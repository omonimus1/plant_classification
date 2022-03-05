from rest_framework import serializers
from .models import Prediction, Result
from django.db import models


class GetPredictionSerializer(serializers.ModelSerializer):
    image = models.ImageField(upload_to="img/%Y/%m/%d/", blank=False)
    class Meta:
        model = Prediction
        fields = ['image']


class PredictionSerializer(serializers.ModelSerializer):
    image = models.ForeignKey(Prediction, on_delete=models.CASCADE)
    expected_result = models.CharField(
        max_length=100, blank=True, null=False, default=""
    )
    class Meta:
        model = Result
        fields = "__all__"