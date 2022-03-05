
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import predictor
from .models import Prediction, Result
from .serializers import PredictionSerializer, GetPredictionSerializer
from django.core.files.storage import default_storage
from rest_framework.generics import GenericAPIView
import os
import pickle
from . import predictor
import numpy as np
from django.core.files.storage import default_storage
from django.shortcuts import render
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image
from .models import Prediction
from django.http import HttpRequest
from rest_framework.request import Request


module_dir = os.path.dirname(__file__)  # get current directory
module_path = os.path.join(module_dir, "classifier.pkl")
model = Sequential()
current_directory = os.getcwd()
model_path = current_directory + "classifier.pkl"
model = pickle.load(
    open(
        module_path,
        "rb",
    )
)
class GetPredictionApi(APIView):
    serializer_class = GetPredictionSerializer
    queryset = Prediction.objects.all()

    def post(self, request):

        image = request.FILES["image"]
        name = default_storage.save(image.name, image)
        data = {"name": name, "image": image}
        serializer = GetPredictionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            file_url = default_storage.path(name)
            img = image.load_img(file_url, target_size=(150, 150))
            img_array = image.img_to_array(img)
            img_batch = np.expand_dims(img_array, axis=0)
            prediction = model.predict(img_batch)
            pred_digits = np.argmax(prediction, axis=1)
            print(pred_digits)
            response = {
                # "image": file_url,
                "predictions": predictor.flower_identification[pred_digits[0]],
            }
            return Response(
                {"status": "success", "data": '1'}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
    

class PredictionFeedbackApi(GenericAPIView):
    serializer_class = PredictionSerializer
    queryset = Result.objects.all()

    def post(self, request):
        serializer = PredictionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )