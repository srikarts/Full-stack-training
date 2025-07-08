from django.urls import path
from . import views

urlpatterns = [
    path('insert_employee/',views.insert_employee,name='insert_employee'),
    path('view_employee/',views.view_employee,name='view_employee'),
    path('first_101/',views.first_101,name='first_101'),
    path('first_102/',views.first_102,name='first_102'),
    path('first_103/',views.first_103,name='first_103'),
    path('first_104/',views.first_104,name='first_104'),
    path('first_105/',views.first_105,name='first_105'),
    path('firstp_101P/',views.firstp_101P,name='firstp_101P'),
    path('firstp_102P/',views.firstp_102P,name='firstp_102P'),
    path('firstp_103P/',views.firstp_103P,name='firstp_103P'),
    path('render_success/',views.insert_employee,name='insert_employee')
]