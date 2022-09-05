from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # login page
    return HttpResponse('<h1>login</h1>')

def reg(request):
    # show all subject the user apply
    return HttpResponse('<h1>Reg</h1>')