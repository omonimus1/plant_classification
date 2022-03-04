import os
import pickle

import numpy as np
from django.core.files.storage import default_storage
from django.shortcuts import render
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import predictor
from .models import Prediction
from .serializers import PredictionSerializer

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


# Create your views here.
def IndexView(request):
    return render(request, "index.html")


def ImageView(request):
    if request.method == "POST":
        file = request.FILES["imageFile"]
        file_name = default_storage.save(file.name, file)

        prediction_request = Prediction.objects.create(name=file_name, image=file)
        prediction_request.save()
        file_url = default_storage.path(file_name)
        img = image.load_img(file_url, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_batch = np.expand_dims(img_array, axis=0)
        prediction = model.predict(img_batch)
        pred_digits = np.argmax(prediction, axis=1)
        prediction = predictor.flower_identification[pred_digits[0]]
        Prediction.objects.filter(pk=prediction_request.pk).update(predicted=prediction)
        print(pred_digits)
        return render(
            request,
            "upload.html",
            {
                "predictions": prediction,
                "image": file_url,
                "id": prediction_request.pk
            },
        )
    else:
        return render(request, "upload.html")


def Display(request):
    if request.method == "GET":
        return render(request, "display.html")


def thanks(request):
    return render(request, "thank-you.html")

class GetPredictionApi(APIView):
    serializer_class = PredictionSerializer
    queryset = Prediction.objects.all()

    def post(self, request):

        image = request.FILES["imageFile"]
        name = default_storage.save(image.name, image)
        data = {"name": name, "image": image}
        serializer = PredictionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            Prediction.objects.create(name=name, image=image)

            file_url = default_storage.path(name)
            img = image.load_img(file_url, target_size=(150, 150))
            img_array = image.img_to_array(img)
            img_batch = np.expand_dims(img_array, axis=0)
            prediction = model.predict(img_batch)
            pred_digits = np.argmax(prediction, axis=1)
            print(pred_digits)
            response = {
                "image": file_url,
                "predictions": predictor.flower_identification[pred_digits[0]],
            }
            return Response(
                {"status": "success", "data": response}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
