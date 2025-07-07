from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import StudentModel
# Create your views here.

def list_students(request):
    students = StudentModel.objects.all()
    return render(request,'list.html',{'students':students})

def add_student(request):
    if request.method == 'POST':
        rollno = request.POST['rollno']
        name = request.POST['name']
        marks = request.POST['marks']
        StudentModel.objects.create(rollno=rollno,name=name,marks=marks)
        return redirect('list_students')
    return render(request,'add.html')

def edit_student(request,rollno):
    student = StudentModel.objects.get(rollno=rollno)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.marks = request.POST['marks']
        student.save()
        return redirect('list_students')
    return render(request,'edit.html',{'student':student})

def delete_student(request,rollno):
    student = StudentModel.objects.get(rollno = rollno)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request,'delete.html',{'student':student})

def addnum(request):
    return render(request,'js_add_2_num.html')