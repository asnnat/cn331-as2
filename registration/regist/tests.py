from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from .models import Student, Subject, Register
from .views import index, subject, mysubject

class TestUrl(SimpleTestCase):
    def test_index_is_resolved(self):
        url = reverse('regist:index')
        self.assertEqual(resolve(url).func, index)

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.index_url = reverse('regist:index')

    def test_index(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'regist/index.html')