from django.db import models


class Prediction(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="img/%Y/%m/%d/", blank=False)


    def __str__(self):
        return self.name

class Result(models.Model):
    imagine = models.ForeignKey(Prediction, on_delete=models.CASCADE)
    expected_result = models.CharField(
        max_length=100, blank=True, null=False, default=""
    )
    prediction_feedback = models.BooleanField(blank=True, null=False, default=False)
    def __str__(self):
        return self.result


class UserContactRequest(models.Model):
    name = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)
    message = models.TextField(blank=False, null=False, default='No message content given')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
