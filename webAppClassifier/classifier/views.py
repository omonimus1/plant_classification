import os
import pickle
import numpy as np
from django.core.files.storage import default_storage
from django.shortcuts import render
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image
from . import predictor
from .models import FavoritePrediction
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .models import Prediction
from django.contrib.auth import logout

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


def Index(request):
    return render(request, "index.html")


def ImageView(request):
    if request.method == "POST":
        file = request.FILES["imageFile"]
        file_name = default_storage.save(file.name, file)

        file_url = default_storage.path(file_name)
        img = image.load_img(file_url, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_batch = np.expand_dims(img_array, axis=0)
        prediction = model.predict(img_batch)
        pred_digits = np.argmax(prediction, axis=1)
        print(pred_digits)
        p = Prediction.objects.create(
            name=predictor.flower_identification[pred_digits[0]], image=file
        )
        p.save()
        return render(
            request,
            "upload.html",
            {
                "predictions": predictor.flower_identification[pred_digits[0]],
                "id": p.pk,
            },
        )
    return render(request, "upload.html")


def Display(request):
    if request.method == "GET":
        return render(request, "display.html")


def thanks(request):
    return render(request, "thank-you.html")


def loginView(request):
    if request.method == "POST":
        username = request.POST["username_login"]
        password = request.POST["password_login"]
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(request, "index.html")


def favoriteView(request):
    # get All my favorite
    user_favorite = FavoritePrediction.objects.filter(user=request.user.pk)
    return render(
        request,
        "favorite.html",
        {
            "favorite": user_favorite,
        },
    )


def logoutView(request):
    logout(request)
    return render(request, "index.html")


def contact(request):
    if request.method == "POST":
        message = request.POST["message"]
        email = request.POST["email"]
        if message and email:
            try:
                send_mail(
                    "Email from Plat classifier",
                    message,
                    email,
                    ["davidepollicino2015@gmail.com"],
                    fail_silently=False,
                )
            except Exception:
                return HttpResponse("Error while sending email")
            return HttpResponse("Thanks for have contact us")
        else:
            return HttpResponse("Make sure all fields are entered and valid.")
    return render(request, "index.html")
