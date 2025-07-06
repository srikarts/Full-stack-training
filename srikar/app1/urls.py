from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('',views.page,name='page'),
    path('demo/',views.demo,name='demo'),
]
