from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from django.core import mail
from .views import Index, ImageView
from django.contrib.auth.models import User
from .models import Prediction, Result, FavoritePrediction
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile


def create_image():
    image = Image.new("RGBA", size=(50, 50), color=(256, 0, 0))
    image_file = io.BytesIO(image.tobytes("hex", "rgb"))
    file = InMemoryUploadedFile(image_file, None, "test.jpg", "image/jpg", 1024, None)
    return file


class ImageViewTestCase(TestCase):
    longMessage = True

    def test_get(self):
        req = RequestFactory().get("upload")
        req.user = AnonymousUser()
        resp = ImageView(req, *[], **{})
        self.assertEqual(resp.status_code, 200)


class IndexViewTestCase(TestCase):
    longMessage = True

    def test_get(self):
        req = RequestFactory().get("")
        req.user = AnonymousUser()
        resp = Index(req, *[], **{})
        self.assertEqual(resp.status_code, 200)


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get("http://127.0.0.1:8000/")
        self.assertEqual(response.status_code, 200)


class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail(
            "New Email from flower classifier web app",
            "Hi Davide, this is a test email",
            "flowerclassifier@gmail.com",
            ["davidepollicino2015@gmail.com.com"],
            fail_silently=False,
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            mail.outbox[0].subject, "New Email from flower classifier web app"
        )


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            first_name="davide",
            last_name="pollicino",
            username="davidetest",
            email="davide@test.com",
            password="123456",
        )

    def test_name_user(self):
        user = User.objects.get(id=1)
        self.assertEquals(user.first_name, "davide")
        self.assertEquals(user.last_name, "pollicino")
        self.assertEquals(user.username, "davidetest")
        self.assertEquals(user.email, "davide@test.com")


class PredictionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        image = Image.new("RGBA", size=(50, 50), color=(256, 0, 0))
        image_file = io.BytesIO(image.tobytes("hex", "rgb"))
        file = InMemoryUploadedFile(
            image_file, None, "test.jpg", "image/jpg", 1024, None
        )
        p = Prediction.objects.create(image=file, name="rose")
        p.save()

    def test_prediction_record(self):
        prediction = Prediction.objects.get(pk=1)
        self.assertEquals(prediction.name, "rose")


class ResultModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        file = create_image()
        p = Prediction.objects.create(image=file, name="rose")
        p.save()
        result = Result.objects.create(
            image=p, expected_result="I was expecting a rose"
        )
        result.save()

    def test_feedback_record(self):
        result = Result.objects.get(pk=1)
        self.assertEquals(result.image.name, "rose")
        self.assertEquals(result.expected_result, "I was expecting a rose")
        max_length = result._meta.get_field("expected_result").max_length
        self.assertEquals(max_length, 200)


class FavoriteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        file = create_image()
        p = Prediction.objects.create(image=file, name="rose")
        p.save()
        user = User.objects.create(
            first_name="davide",
            last_name="pollicino",
            username="davide",
            email="davide@test.com",
            password="123456",
        )
        user.save()
        favorite = FavoritePrediction.objects.create(user=user, prediction=p)
        favorite.save()

    def test_feedback_record(self):
        favorite = FavoritePrediction.objects.get(pk=1)
        self.assertEquals(favorite.user.username, "davide")
        self.assertEquals(favorite.prediction.name, "rose")
        self.assertEquals(favorite.user.first_name, "davide")
