from django.db import models

# models.py
class Profile(models.Model):
    image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=False)
    name = models.CharField(max_length=100, blank=False)
