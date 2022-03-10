from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Prediction(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="img/%Y/%m/%d/", blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name + " " + str(self.pk)


class Result(models.Model):
    image = models.ForeignKey(Prediction, on_delete=models.CASCADE)
    expected_result = models.CharField(
        max_length=200, blank=True, null=False, default=""
    )
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.expected_result


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    prediction = models.ForeignKey(Prediction, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.user.username
