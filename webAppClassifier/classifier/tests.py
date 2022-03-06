from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase

from .views import Index, ImageView


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
