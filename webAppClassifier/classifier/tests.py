from django.test import TestCase
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from .models import UserContactRequest
from .views import IndexView, ImageView

<<<<<<< HEAD

class UserContactTest(TestCase):
    @classmethod
    def setUp(self):
        UserContactRequest.objects.create(
            name="Davide", message="Hi, is prediction working?"
        )

    def testSupportUserName(self):
        userRequest = UserContactRequest.objects.get(pk=1)
        self.assertEquals(userRequest.name, "Davide")


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
        resp = IndexView(req, *[], **{})
        self.assertEqual(resp.status_code, 200)
=======
# Create your tests here.
class AnimalTestCase(TestCase):

    def test_animals_can_speak(self):
        self.assertEqual('hello', 'hello')
>>>>>>> dev
