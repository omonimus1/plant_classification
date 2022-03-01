# forms.py
from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ["image", "name"]
