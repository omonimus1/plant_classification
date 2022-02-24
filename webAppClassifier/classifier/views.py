from re import template
from django.shortcuts import render
from django.views.generic import DetailView
from .forms import ProfileForm
from .models import Prediction
from .api import  ClassifyFlowerAPI, predict_image
# Create your views here.
def Index(request):
    return render(request, 'index.html')


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
from keras.preprocessing.image import ImageDataGenerator,load_img, img_to_array
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras import optimizers
import os

model = Sequential()
current_directory = os.getcwd()
model_path = current_directory+'classifier.pkl'
model = pickle.load(open('/Users/davide/Desktop/university/honours/plant_classification/webAppClassifier/classifier/classifier.pkl', 'rb'))


def ImageView(request):
    if request.method == 'POST':
        profile_form = ProfileForm(data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            img_obj = profile_form.instance

            # predict_image('http://127.0.0.1:8000'+img_obj.image.url)
            # image_array = asarray(img_obj)
            # img = image.load_img('http://127.0.0.1:8000'+img_obj.image.url, target_size=(150, 150))
            # picture = open('http://127.0.0.1:8000'+img_obj.image.url)
            """
            picture = os.path.join(os.path.dirname(os.path.dirname('http://127.0.0.1:8000'+img_obj.image.url)))
            img = image.load_img(picture, target_size=(150, 150))
            img_array = image.img_to_array(img)
            img_batch = np.expand_dims(img_array, axis=0)
            prediction = model.predict(img_batch)
            pred_digits=np.argmax(prediction,axis=1)
            print(pred_digits)
            """
            return render(request, 'upload.html', {'profile_form': profile_form, 'img_obj': img_obj})
    else:
        profile_form = ProfileForm()
        return render(request, 'upload.html', {'profile_form': profile_form})

def Display(request):
    if request.method == 'GET':
        img = Prediction.objects.all()
        return render(request, 'display.html', {'profile_img': img})