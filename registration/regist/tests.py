from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve

from django.contrib.auth.models import User
from .models import Student, Subject, Register
from .views import index, subject, register, mysubject, removesubject

class TestUrl(SimpleTestCase):
    def test_index_is_resolved(self):
        url = reverse('regist:index')
        self.assertEqual(resolve(url).func, index)

    def test_subject_is_resolved(self):
        url = reverse('regist:subject', args=[1])
        self.assertEqual(resolve(url).func, subject)
        
    def test_register_is_resolved(self):
        url = reverse('regist:register', args=[1])
        self.assertEqual(resolve(url).func, register)
        
    def test_mysubject_is_resolved(self):
        url = reverse('regist:mysubject')
        self.assertEqual(resolve(url).func, mysubject)

    def test_removesubject_is_resolved(self):
        url = reverse('regist:removesubject', args=[1])
        self.assertEqual(resolve(url).func, removesubject) 

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

        self.student = Student.objects.create(username=self.username, first=self.first, last=self.last)
        self.subject = Subject.objects.create(
            code='CN101',
            name='INTRODUCTION TO COMPUTER PROGRAMMING',
            semester=1,
            year=2566,
            max_cap=5,
            status=True
        )
        self.regist = Register.objects.create(student=self.student, subject=self.subject)

        self.index_url = reverse('regist:index')
        self.subject_url = reverse('regist:subject', args=[self.subject.id])
        self.register_url = reverse('regist:register', args=[self.subject.id])
        self.mysubject_url = reverse('regist:mysubject')
        self.removesubject_url = reverse('regist:removesubject', args=[self.regist.id])

    def test_index(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'regist/index.html')

    def test_subject(self):
        response = self.client.get(self.subject_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'regist/subject.html')

    # def test_register(self):
    #     response = self.client.post(self.register_url)

    #     self.assertEqual(response.status_code, 200)

    def test_mysubject(self):
        response = self.client.get(self.mysubject_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'regist/mysubject.html')

    def test_removesubject_already_registed(self):
        response = self.client.delete(self.removesubject_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'regist/mysubject.html')

    def test_removesubject_no_regist(self):
        # cannot be POST
        response = self.client.get(self.removesubject_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'regist/mysubject.html')