from django.db import models
from django import forms
class Classification(models.Model):
    image = models.ImageField(upload_to='Flowers')
    correct_prediction = models.BooleanField(default=False)

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title