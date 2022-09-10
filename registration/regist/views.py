from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Student, Subject, Register

def index(request):
    student = Student.objects.filter(pk=request.user.id).first()
    regists = Register.objects.filter(student=student).all()
    subjects = Subject.objects.exclude(pk__in=regists, status=False).all()
    subjects = Subject.objects.filter(status=True).all()

    return render(request, 'regist/index.html', {
        'subjects': subjects,
    })

def subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)

    return render(request, 'regist/subject.html', {
        'subject': subject
    })

def register(request, subject_id):
    student = Student.objects.get(pk=request.user.id)
    subject = Subject.objects.get(pk=subject_id)

    check = Register.objects.filter(student=student, subject=subject).first()
    if not check:
        regist = Register.objects.create(student=student, subject=subject)

        return HttpResponseRedirect(reverse('regist:index'))