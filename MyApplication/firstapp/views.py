from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'firstapp/Home.html',{})

def css(request):
    return render(request,'firstapp/cssfile.html',{})

def js(request):
    return render(request,'firstapp/jsfile.html',{})