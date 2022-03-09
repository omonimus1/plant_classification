from rest_framework import generics
# from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from .models import Result, Prediction
from .serializers import LeaveFeedbackSerializer, RegisterSerializer, UserSerializer
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from django.contrib.auth.models import User

# Prediction Model section

import pickle
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import os

from pathlib import Path


# Specifically for manipulating zipped images and getting numpy arrays of pixel values of images.
import matplotlib.pyplot as plt
import numpy as np


# dl libraries specifically for CNN
from tensorflow.keras.models import Sequential
import os


module_dir = os.path.dirname(__file__)
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


class ClassifyFlowerAPI(generics.GenericAPIView):
    queryset = Prediction.objects.all()
    # serializer_class = UserSerializer
    # permission_classes = [IsActive, IsAuthenticated,]

    def post(self, request):
        file = request.FILES["imageFile"]
        file_name = default_storage.save(file.name, file)

        p = Prediction.objects.create(name=file_name, image=file)
        p.save()
        file_url = default_storage.path(file_name)
        img = image.load_img(file_url, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_batch = np.expand_dims(img_array, axis=0)
        prediction = model.predict(img_batch)
        pred_digits = np.argmax(prediction, axis=1)
        print(pred_digits)
        return JsonRespons(
        {"predictions": predictor.flower_identification[pred_digits[0]], "id": p.pk},
        )


def predict_image(img_array):
    print("ciao")
    img_path = picture_url
    print('BEFORE LOAD')
    img = image.load_img(img_path, target_size=(150, 150))
    print('BEFORE IMG TO ARRAY')
    img_array = image.img_to_array(img)

    print("BEFORE EXPAND DIMS")
    img_batch = np.expand_dims(img_array, axis=0)
    print("BEFORE PREDICT")
    prediction = model.predict(img_batch)
    print("BEFORE ARGMAX")
    pred_digits = np.argmax(prediction, axis=1)
    print(pred_digits)



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



class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,  context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })