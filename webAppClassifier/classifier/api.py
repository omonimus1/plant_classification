from rest_framework.generics import UpdateAPIView
import json
from django.http.response import JsonResponse
from rest_framework.response import Response
from .models import Prediction

# Prediction Model section
from .forms import ProfileForm

import pickle
from tensorflow.keras.preprocessing import image
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import os
import shutil
from os.path import isfile, join, abspath, exists, isdir, expanduser
from os import listdir, makedirs, getcwd, remove
from pathlib import Path

# Data visualisation
import pandas as pd

# Image manipulation
from PIL import Image
import cv2

# Specifically for manipulating zipped images and getting numpy arrays of pixel values of images.
import matplotlib.pyplot as plt
import matplotlib.image as mimg
import numpy as np

# Plotting library
from mpl_toolkits.mplot3d import Axes3D  # needed to plot 3-D surfaces

# dl libraries specifically for CNN
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras import optimizers
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
    """
    img_path = picture_url
    print('BEFORE LOAD')
    img = image.load_img(img_path, target_size=(150, 150))
    print('BEFORE IMG TO ARRAY')
    img_array = image.img_to_array(img)
    """
    print("BEFORE EXPAND DIMS")
    img_batch = np.expand_dims(img_array, axis=0)
    print("BEFORE PREDICT")
    prediction = model.predict(img_batch)
    print("BEFORE ARGMAX")
    pred_digits = np.argmax(prediction, axis=1)
    print(pred_digits)
