from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('<h1> This is a third trail of starting django project. </h1>')