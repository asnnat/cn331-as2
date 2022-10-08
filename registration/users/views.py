from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from regist.models import Student, Subject
from regist import views
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html',status = 400)
    return render(request, 'regist/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)

            student = Student.objects.filter(username=username).first()
            if not student:
                username = request.user.username
                first = request.user.first_name
                last = request.user.last_name

                student = Student.objects.create(username=username, first=first, last=last)
            return views.index(request)
            # return HttpResponseRedirect(reverse('regist:index'))
        else:
            return render(request, 'users/login.html', {
                'message': 'Invalid credentials.',
                'message_tag': "alert alert-danger",
            },status = 400)
    #return render(request, 'users/login.html')


def logout_view(request):
    logout(request)

    return render(request, 'users/login.html', {
        'message': 'You are logged out.',
        'message_tag': "alert alert-danger"
    })