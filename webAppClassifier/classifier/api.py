"""
from rest_framework.generics import UpdateAPIView
from .models import Prediction

# Prediction Model section
from .forms import ProfileForm

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


model = Sequential()
current_directory = os.getcwd()
model_path = current_directory + "classifier.pkl"
model = pickle.load(
    open(
        "/Users/davide/Desktop/university/honours/plant_classification/webAppClassifier/classifier/classifier.pkl",
        "rb",
    )
)


class ClassifyFlowerAPI(UpdateAPIView):
    queryset = Prediction.objects.all()
    # serializer_class = UserSerializer
    # permission_classes = [IsActive, IsAuthenticated,]

    def post(self, request):
        profile_form = ProfileForm(data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            image = profile_form.instance
            name = "GNAGNA"
            single_prediction = Prediction(name=name, image=image)
            single_prediction.save()
            print(single_prediction.image.url)
            #
            # profile_form.save()
            predict_image(single_prediction.image.url)


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
                {"status": "error", "data": serializer.errors}, status=status.HTTP_200_OK

"""
