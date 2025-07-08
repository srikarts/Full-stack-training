from django.forms import fields
from .models import StudentModel
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel   #specifies the model to be used to create form
        fields = '__all__'    #This includes all the fields of the model


