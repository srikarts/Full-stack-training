from django.shortcuts import render
from .models import EmployeeModel
from .forms import EmployeeForm
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def insert_employee(request):
    context ={}
    ob_form = EmployeeForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return render(request,'render_success.html')
    context['form']=ob_form
    return render(request,'insert_employee.html',context)

def view_employee(request):
    ob = EmployeeModel.objects.all().values()
    context = {
        'data':ob
    }
    temp = loader.get_template('view_employee.html')
    return HttpResponse(temp.render(context,request))

def first_101(request):
    temp = loader.get_template('MCA-101.html')
    return HttpResponse(temp.render())

def first_102(request):
    temp = loader.get_template('MCA-102.html')
    return HttpResponse(temp.render())

def first_103(request):
    temp = loader.get_template('MCA-103.html')
    return HttpResponse(temp.render())

def first_104(request):
    temp = loader.get_template('MCA-104.html')
    return HttpResponse(temp.render())

def first_105(request):
    temp = loader.get_template('MCA-105.html')
    return HttpResponse(temp.render())

def firstp_101P(request):
    temp = loader.get_template('MCA-101P.html')
    return HttpResponse(temp.render())

def firstp_102P(request):
    temp = loader.get_template('MCA-102P.html')
    return HttpResponse(temp.render())

def firstp_103P(request):
    temp = loader.get_template('MCA-103P.html')
    return HttpResponse(temp.render())