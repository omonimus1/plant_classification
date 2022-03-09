from django.db import models
from django.contrib.auth.models import User


class Prediction(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="img/%Y/%m/%d/", blank=False)

    def __str__(self):
        return self.name + ' ' + str(self.pk)


class Result(models.Model):
    image = models.ForeignKey(Prediction, on_delete=models.CASCADE)
    expected_result = models.CharField(
        max_length=200, blank=True, null=False, default=""
    )

    def __str__(self):
        return self.expected_result


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    prediction = models.ForeignKey(Prediction, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username
