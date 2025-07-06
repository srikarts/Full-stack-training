from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def home(request):
    return HttpResponse('<h1> Hello Srikar! This is a new project.</h1>')

def page(request):
    template = loader.get_template('login_form.html')
    return HttpResponse(template.render())

def demo(request):
    temp = loader.get_template('font_tag.html')
    return HttpResponse(temp.render())