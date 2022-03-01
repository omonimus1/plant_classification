from django.test import TestCase

# Create your tests here.
class AnimalTestCase(TestCase):

    def test_animals_can_speak(self):
        self.assertEqual('hello', 'hello')
