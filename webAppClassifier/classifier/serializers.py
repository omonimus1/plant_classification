from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import Prediction, Result


class PredictionSerializer(serializers.ModelSerializer):
    image = models.ImageField(upload_to="img/%Y/%m/%d/", blank=False)

    class Meta:
        model = Prediction
        fields = ("image")


class LeaveFeedbackSerializer(serializers.ModelSerializer):
    image = models.ForeignKey(Prediction, on_delete=models.CASCADE)
    expected_result = models.CharField(
        max_length=100, blank=True, null=False, default=""
    )

    class Meta:
        model = Result
        fields = "__all__"


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }

        def create(self, validated_data):
            user = User.objects.create_user(validated_data['username'],                 
                                            password = validated_data['password'],
                                            first_name=validated_data['first_name'],  
                                            last_name=validated_data['last_name'])
            return user

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'