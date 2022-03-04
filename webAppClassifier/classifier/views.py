import os
import pickle
from . import predictor
import numpy as np
from django.core.files.storage import default_storage
from django.shortcuts import render
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image
from .models import Prediction


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

