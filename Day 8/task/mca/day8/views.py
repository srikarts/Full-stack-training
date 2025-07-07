from django.shortcuts import render
from django.urls import path
from .models import StudentModel
from .forms import StudentForm
from django.http import HttpResponse

def insert_student(request):
    context = {}
    ob_form = StudentForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("<h1> Data Saved Successfully!</h1>")
    context['form']=ob_form
    return render(request, "insert_student.html",context)

