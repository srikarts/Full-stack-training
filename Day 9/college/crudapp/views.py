from django.shortcuts import render
from .models import StudentModel
from .forms import StudentForm
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def add_student(request):
    students = StudentModel.objects.all()
    return render(request,'add_student.html',{'students':students})

def update_student(request):
    pass

def delete_student(request):
    pass

def view_students(request):
    pass

def add_faculty(request):
    pass

def update_faculty(request):
    pass