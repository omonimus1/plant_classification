
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import predictor
from .models import Prediction
from .serializers import PredictionSerializer
from django.core.files.storage import default_storage

class GetPredictionApi(APIView):
    serializer_class = PredictionSerializer
    queryset = Prediction.objects.all()

    def post(self, request):

        image = request.FILES["imageFile"]
        name = default_storage.save(image.name, image)
        data = {"name": name, "image": image}
        serializer = PredictionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            Prediction.objects.create(name=name, image=image)

            file_url = default_storage.path(name)
            img = image.load_img(file_url, target_size=(150, 150))
            img_array = image.img_to_array(img)
            img_batch = np.expand_dims(img_array, axis=0)
            prediction = model.predict(img_batch)
            pred_digits = np.argmax(prediction, axis=1)
            print(pred_digits)
            response = {
                "image": file_url,
                "predictions": predictor.flower_identification[pred_digits[0]],
            }
            return Response(
                {"status": "success", "data": response}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )