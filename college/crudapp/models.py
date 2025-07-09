from django.db import models

# Create your models here.
class StudentModel(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return (self.first_name)+' '+(self.last_name)
    
class EmployeeModel(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return (self.first_name)+' '+(self.last_name)
    
    