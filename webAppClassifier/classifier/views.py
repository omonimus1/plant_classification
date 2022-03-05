import os
import pickle
from . import predictor
import numpy as np
from django.core.files.storage import default_storage
from django.shortcuts import render
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image
from .models import Prediction
from django.http import HttpRequest
from rest_framework.request import Request


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
        print("BEFORE GET IMAGE")
        file = request.FILES["ImageFile"]
        print('IMAGE RECEIVED')

        file_name = default_storage.save(file.name, file)
        file_name='test'
        t = Prediction.objects.create(image = file, name=file_name)
        t.save()
        print(t.pk)
        print(t.image.url)
        print(t.image)
        # Prediction.objects.create(name=file_name, image=file)
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
        return render(request, "display.html")


def thanks(request):
    return render(request, "thank-you.html")

