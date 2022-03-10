from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from django.core import mail
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


class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            ["to@example.com"],
            fail_silently=False,
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Subject here")
