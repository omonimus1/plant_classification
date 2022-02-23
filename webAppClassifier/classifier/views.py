from cv2 import FarnebackOpticalFlow_create
from django.shortcuts import render
from django.http import HttpResponse
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Sequential
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
## Define models and load
import pickle
model = Sequential()
model = pickle.load(open('/Users/davide/Desktop/university/honours/plant_classification/webAppClassifier/classifier/classifier.pkl', 'rb'))
flower_identification = {
    0: 'Dandelion',
    1: 'Tulip',
    2: 'Rose',
    3: 'Daisy',
    4: 'Sunflower'
}


from django.shortcuts import render
from .forms import ImageForm

def identify_flower():

    img_path = "/Users/davide/Desktop/university/honours/plant_classification/webAppClassifier/classifier/static/i/sunflower.jpeg"
    # plt.show(img_path)
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    # img_preprocessed = preprocess_input(img_batch)

    # load model here 
    prediction = model.predict(img_batch)
    pred_digits=np.argmax(prediction,axis=1)
    print(pred_digits)
    # Name of the predicted flower
    # print('Plant name: ' + flower_identification[pred_digits[0]])
    # Get Percentage of predictions 
    predict_classes=np.argmax(prediction,axis=1)
    print(predict_classes)
    # Predict model


def Home(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})

def upload(request):
    print('inside upload')
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        form.save()
        print('saved form')
        # Get the current instance object to display in the template
        img_obj = form.instance
        print('returned image')
        return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        print('not inside POST upload section')
        form = ImageForm()
    return render(request, 'index.html', {'form': form})