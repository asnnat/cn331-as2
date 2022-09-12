from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Student, Subject, Register

def index(request):
    student = Student.objects.filter(username=request.user.username).first()
    regists = Register.objects.filter(student=student).all()

    id = []
    for regist in regists:
        id.append(regist.subject.id)
    subjects = Subject.objects.exclude(pk__in=id)

    return render(request, 'regist/index.html', {
        'subjects': subjects,
    })

def subject(request, subject_id):
    student = Student.objects.filter(username=request.user.username).first()
    subject = Subject.objects.get(id=subject_id)
    regists = Register.objects.filter(subject=subject).all()
    registed = Register.objects.filter(student=student, subject=subject).first()

    return render(request, 'regist/subject.html', {
        'subject': subject,
        'count': len(regists),
        'registed': registed
    })

def register(request, subject_id):
    student = Student.objects.get(username=request.user.username)
    subject = Subject.objects.get(pk=subject_id)

    check = Register.objects.filter(student=student, subject=subject).first()
    if not check:
        regist = Register.objects.create(student=student, subject=subject)

        return HttpResponseRedirect(reverse('regist:mysubject'))

def mysubject(request):
    student = Student.objects.get(username=request.user.username)
    regists = Register.objects.filter(student=student).all()

    return render(request, 'regist/mysubject.html', {
        'regists': regists,
    })

def removesubject(request, subject_id):
    student = Student.objects.get(username=request.user.username)
    subject = Subject.objects.get(pk=subject_id)
    regist = Register.objects.get(student=student, subject=subject)

    if regist:
        unregist = regist.delete()
        if unregist:
            return HttpResponseRedirect(reverse('regist:mysubject'))