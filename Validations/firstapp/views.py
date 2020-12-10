from django.shortcuts import render,redirect
from django.http import HttpResponse
from firstapp.forms import RegisterForm
# Create your views here.

def Reg(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Registered Successfully")
	form = RegisterForm()
	return render(request, 'firstapp/index.html',{'form':form})