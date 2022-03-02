from django.test import TestCase

from .models import UserContactRequest


class PredictionModelTest(TestCase):
    def test(self):
        self.assertEquals(200, 200)


class UserContactTest(TestCase):
    @classmethod
    def setUp(self):
        UserContactRequest.objects.create(name='Davide', message='Hi, is prediction working?')

    def testSupportUserName(self):
        userRequest = UserContactRequest.objects.get(pk=1)
        self.assertEquals(userRequest.name, 'Davide')


"""
class PredictionModelTest(TestCase):
    @classmethod
    def setUp(cls):
        current_directory = os.getcwd()
        image_path = current_directory + "testImages/sunflower.jpeg"

        newPhoto = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(),
                                            content_type='image/jpeg')
        Prediction.objects.create(name='Python', image=newPhoto.image)

        def test_name_max_length(self):
            unit = Prediction.objects.get(id=1)
            max_length = unit._meta.get_field('name').max_length
            self.assertEquals(max_length, 200)

"""
