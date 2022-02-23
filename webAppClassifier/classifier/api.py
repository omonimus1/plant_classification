from rest_framework.generics import UpdateAPIView
import json
from django.http.response import JsonResponse
from rest_framework.response import Response
from .models import Prediction

class ClassifyFlowerAPI(UpdateAPIView):
    queryset = Prediction.objects.all()
    # serializer_class = UserSerializer
    # permission_classes = [IsActive, IsAuthenticated,]

    def post(self, request):
        pass
