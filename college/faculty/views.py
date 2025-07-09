from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1> Faculty app created Successfully. </h1>')

def index(request):
    return HttpResponse('<h1> This is an index page of the college app. </h1>')
