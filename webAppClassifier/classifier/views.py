from django.shortcuts import render
from django.http import HttpResponse
from tensorflow.keras.preprocessing import image
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

"""
img_path = "/content/gdrive/Othercomputers/DavideLaptop/Desktop/flowersData/sunflower/23286304156_3635f7de05.jpg"
plt.show(img_path)
img = image.load_img(img_path, target_size=(150, 150))
img_array = image.img_to_array(img)
img_batch = np.expand_dims(img_array, axis=0)
# img_preprocessed = preprocess_input(img_batch)

# load model here 
prediction = model.predict(img_batch)
pred_digits=np.argmax(prediction,axis=1)
print(pred_digits)
# Name of the predicted flower
print('Plant name: ' + flower_identification[pred_digits[0]])
# Get Percentage of predictions 
predict_classes=np.argmax(prediction,axis=1)
print(predict_classes)
# Predict model
"""
def Home(request):
    return render(request, 'index.html')