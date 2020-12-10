from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile

from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(req):
	return render(req,'accounts/home.html',{})

def register(req):
	if req.method=="POST":
		fname=req.POST.get('first_name')
		lname=req.POST.get('last_name')
		uname=req.POST.get('username')
		email=req.POST.get('email')
		pwd=req.POST.get('pwd')
		img=req.FILES.get('image')

		user_id=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pwd)
		UserProfile.objects.create(user_id=user_id,image=img)
		return HttpResponse('Successfully created..!')
	return render(req,'accounts/register.html')

def signin(req):
	if req.method=="POST":
		un=req.POST.get('username')
		pwd=req.POST.get('password')
		user=authenticate(username=un,password=pwd)
		if user:
			login(req,user)
			return redirect('/')

	return render(req,'accounts/signin.html')