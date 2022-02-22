from django.db import models

class Classification(models.Model):
    image = models.ImageField(upload_to='Flowers')
    correct_prediction = models.BooleanField(default=False)