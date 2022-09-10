from django.urls import path

from . import views

app_name = 'regist'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:subject_id>', views.subject, name='subject'),
    path('new/<int:subject_id>', views.register, name='register'),
]