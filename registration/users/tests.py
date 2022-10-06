from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import index, login_view, logout_view

class TestUrl(SimpleTestCase):
    def test_index_is_resolved(self):
        url = reverse('users:index')
        self.assertEqual(resolve(url).func, index)

    def test_login_is_resolved(self):
        url = reverse('users:login')
        self.assertEqual(resolve(url).func, login_view)

    def test_logout_is_resolved(self):
        url = reverse('users:logout')
        self.assertEqual(resolve(url).func, logout_view)

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.username = 'testuser'
        self.password = 'secret'
        self.email = 'testuser@bookingreg.com'
        self.first = 'Test'
        self.last = 'User'
        self.credentials = {
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'first_name': self.first,
            'last_name': self.last}
        self.new_user = User.objects.create_user(**self.credentials)

        self.index_url = reverse('regist:index')

    def test_login_is_success(self):
        url = reverse('users:login')
        response = self.client.post(url, {
            'username': 'testuser',
            'password': 'secret'
        })

        self.assertEqual(response.status_code, 200)

    def test_login_is_unsuccess(self):
        url = reverse('users:login')
        response = self.client.post(url, {
            'username': 'testuser',
            'password': 'notsecret'
        })

        self.assertEqual(response.status_code, 400)

    def test_logout_is_success(self):
        url = reverse("users:logout")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)