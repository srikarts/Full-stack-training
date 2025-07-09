from django.urls import path
from . import views

urlpatterns = [
    path('add_student/',views.add_student,name='add_student'),
    path('update_student/<int:id>',views.update_student,name='update_student'),
    path('delete_student/<int:id>',views.delete_student,name='delete_student'),
    path('list_students/',views.list_students,name='list_students'),
]