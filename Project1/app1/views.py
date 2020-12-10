from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>This is Website</h1>")

def mypage(request):
    return render(request,'app1/mypage.html')

def index(request):
    return render(request,'app1/index.html')

def table(request):
    return render(request,'app1/table.html')