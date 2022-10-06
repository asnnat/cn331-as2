from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Student, Subject, Register

def index(request):
    student = Student.objects.filter(username=request.user.username).first()
    regists = Register.objects.filter(student=student).all()

    id = []
    for regist in regists:
        id.append(regist.subject.id)
    subjects = Subject.objects.exclude(pk__in=id).filter(status=True)

    return render(request, 'regist/index.html', {
        'subjects': subjects
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
    if request.method == 'POST':
        student = Student.objects.filter(username=request.user.username).first()
        subject = Subject.objects.filter(pk=subject_id).first()\

        check = Register.objects.filter(student=student, subject=subject).first()
        if check is None:
            Register.objects.create(student=student, subject=subject)

            # return HttpResponseRedirect(reverse('regist:mysubject'))
            return mysubject(request, {
                'message': 'Regist {} success'.format(subject),
                'message_tag': "alert alert-success"
            })
        else:
            return render(request, 'regist/index.html', status=400)
    else:
        return render(request, 'regist/index.html', status=400)

def mysubject(request, message=None):
    student = Student.objects.filter(username=request.user.username).first()
    regists = Register.objects.filter(student=student).all()

    return render(request, 'regist/mysubject.html', {
        'regists': regists,
        'message': message
    })

def removesubject(request, subject_id):
    if request.method == 'POST':
        student = Student.objects.filter(username=request.user.username).first()
        subject = Subject.objects.filter(pk=subject_id).first()
        regist = Register.objects.filter(student=student, subject=subject).first()

        if regist is not None:
            regist.delete()

            return mysubject(request, {
                'message': 'Remove {} success'.format(subject),
                'message_tag': "alert alert-danger"
            })
        else:
            return render(request, 'regist/mysubject.html', status=400)
    else:
        return render(request, 'regist/mysubject.html', status=400)