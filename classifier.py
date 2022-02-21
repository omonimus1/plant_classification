import os
import shutil
from os.path import isfile, join, abspath, exists, isdir, expanduser
from os import listdir, makedirs, getcwd, remove
from pathlib import Path

# Data visualisation 
import pandas as pd 
import seaborn as sns

# Image manipulation
from PIL import Image
from skimage.io import imread
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

# training set
from keras.utils.np_utils import to_categorical
from sklearn.model_selection import train_test_split

# Tells matplotlib to embed plots within the notebook
import math


from google.colab import drive
drive.mount('/content/gdrive/', force_remount=True)

"""from google.colab import auth 
auth.authenticate_user()

project_id = 'plant-classifier'
!gcloud config set project {project_id}
!gsutil ls

bucket_name = 'plant-identification-bucket'
!gsutil -m cp -r /content/gdrive/Othercomputers/DavideLaptop/Desktop/flowersData* gs://{bucket_name}/
"""
print(os.listdir('/content/gdrive/Othercomputers/DavideLaptop/Desktop'))


flowersPath = Path('/content/gdrive/Othercomputers/DavideLaptop/Desktop/flowersData')

flowers = os.listdir(flowersPath)
print("Number of types of flowers: ", len(flowers))
print("Types of flowers: ", flowers)
# A list which contains tuples, the type of flower and the corresponding image path
flowersList = []

for species in flowers:
    # Get all the file names
    allFlowers = os.listdir(flowersPath / species)
    # Add them to the list
    for flower in allFlowers:
        flowersList.append((species, str(flowersPath /species) + '/' + flower))

# Build a dataframe   
# load the dataset as a pandas data frame     
flowersList = pd.DataFrame(data=flowersList, columns=['category', 'image'], index=None)
flowersList.head()


# Load ML model and make a prediction
import pickle
from tensorflow.keras.preprocessing import image
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
filename = '/content/gdrive/Othercomputers/DavideLaptop/Desktop/flowersData/sunflower/23286304156_3635f7de05.jpg'
model = pickle.load(open('/content/gdrive/Othercomputers/DavideLaptop/Desktop/classifier.pkl', 'rb'))

img_path = "/content/gdrive/Othercomputers/DavideLaptop/Desktop/flowersData/sunflower/23286304156_3635f7de05.jpg"
plt.show(img_path)
img = image.load_img(img_path, target_size=(150, 150))
img_array = image.img_to_array(img)
img_batch = np.expand_dims(img_array, axis=0)
prediction = model.predict(img_batch)
pred_digits=np.argmax(prediction,axis=1)
print(pred_digits)
# Name of the predicted flower
# print('Plant name: ' + flower_identification[pred_digits[0]])