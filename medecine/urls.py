from django import views
from django.urls import path
from medecine import views

urlpatterns = [
    path('', views.index, name='index'),
   
  
]