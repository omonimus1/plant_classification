import os
import pickle

import numpy as np
from django.core.files.storage import default_storage
from django.http import JsonResponse
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image

from . import predictor
from .models import Result, Prediction
from .serializers import LeaveFeedbackSerializer, PredictionSerializer

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


class PredictionAPI(generics.GenericAPIView):
    serializer_class = PredictionSerializer
    queryset = Prediction.objects.all()

    def post(self, request):
        file = request.FILES.get["imageFile"]
        print('GOT FILE')
        file_name = default_storage.save(file.name, file)
        p = Prediction.objects.create(name='file_name', image=file)
        p.save()
        print('AFTER SAVE')
        file_url = default_storage.path(p.image)
        img = image.load_img(file_url, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_batch = np.expand_dims(img_array, axis=0)
        prediction = model.predict(img_batch)
        pred_digits = np.argmax(prediction, axis=1)
        print(pred_digits)
        data = {
            "predictions": predictor.flower_identification[pred_digits[0]],
            "id": p.pk
        }

        return JsonResponse(data, status=status.HTTP_200_OK)


class PredictionFeedbackApi(generics.GenericAPIView):
    serializer_class = LeaveFeedbackSerializer
    queryset = Result.objects.all()

    def post(self, request):
        serializer = LeaveFeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors}, status=status.HTTP_200_OK)
