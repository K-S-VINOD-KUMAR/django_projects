from django.contrib import admin
from django.urls import path
import DemoApp import views

urlpatterns = [
    path('index/',views.index,name = 'index'),
    path('fname/',views.fname,name="fname"),
    path('empnumber/',views.empnumber,name="empnumber"),
]
