
import pickle
import os
import numpy as np
from .models import Prediction
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Sequential
from django.shortcuts import render
from django.core.files.storage import default_storage
from . import predictor

model = Sequential()
current_directory = os.getcwd()
model_path = current_directory + "classifier.pkl"
model = pickle.load(
    open(
        "/Users/davide/Desktop/university/honours/plant_classification/webAppClassifier/classifier/classifier.pkl",
        "rb",
    )
)


# Create your views here.
def Index(request):
    return render(request, "index.html")


def ImageView(request):
    if request.method == "POST":
        file = request.FILES["imageFile"]
        file_name = default_storage.save(file.name, file)

        Prediction.objects.create(name=file_name, image=file)

        file_url = default_storage.path(file_name)
        img = image.load_img(file_url, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_batch = np.expand_dims(img_array, axis=0)
        prediction = model.predict(img_batch)
        pred_digits = np.argmax(prediction, axis=1)
        print(pred_digits)
        return render(
            request,
            "upload.html",
            {
                "predictions": predictor.flower_identification[pred_digits[0]],
                "image": file_url,
            },
        )
    else:
        return render(request, "upload.html")


def Display(request):
    if request.method == "GET":
        img = Prediction.objects.all()
        return render(request, "display.html", {"profile_img": img})
