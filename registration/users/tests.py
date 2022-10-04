from django.test import TestCase

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
    pass