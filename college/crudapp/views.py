from django.shortcuts import render,redirect
from .models import StudentModel
from .forms import StudentForm
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def home(request):
    if request.method == 'POST':
        pass
def add_student(request):
    if request.method == 'POST':
        id = request.POST['id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        course = request.POST['course']
        email = request.POST['email']
        StudentModel.objects.create(id=id,first_name=first_name,last_name=last_name,course=course,email=email)
        return redirect('list_students')
    return render(request,'add_student.html')

def update_student(request,id):
    student = StudentModel.objects.get(id=id)
    if request.method == 'POST':
        student.first_name = request.POST['first_name']
        student.email = request.POST['email']
        student.save()
        return redirect('list_students')
    return render(request,'edit_student.html',{'student':student})

def delete_student(request,id):
    student = StudentModel.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request,'delete_student.html',{'student':student})

def list_students(request):
    students = StudentModel.objects.all()
    return render(request,'list_students.html',{'students':students})

# def add_faculty(request):
#     pass

# def update_faculty(request):
#     pass

# def delete_faculty(request):
#     pass

# def view_faculty(reqeust):
#     pass