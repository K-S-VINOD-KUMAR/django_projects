from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h2>Welcome Django Workshop</h2>")

def name(request,n):
    n = "Vinod Kumar"
    return HttpResponse('<h1>My name is {}</h1>'.format(n))

def empnumber(request,emp):
    return HttpResponse('<h1> This is My empnumber {}'.format(emp))

def empdata(request,n,empno):
    return HttpResponse('<h1>My Name is {} and my empnumber is  {}'.format(n,empno))

def wish(request,greet,person,num):
    return HttpResponse('<h1>Hello {} ,My name is {} and Rollno is {}'.format(greet,person,num))