from django.shortcuts import render,redirect
from django.http import HttpResponse
from Tollywood.models import *
from Tollywood.forms import *


# Create your views here.
def home(req):
    return render(req,'app/home.html',{})

def about(req):
    return render(req,'app/about.html',{})

def contact(req):
    return render(req,'app/contact.html',{})

def data(req):
    info = Movieregister.objects.all()
    return render(req,'app/data.html',{'data':info})

def edit(req,id):
    data=Movieregister.objects.get(id=id)
    return render(req,'app/edit.html',{'data':data})

def update(req,id):
    if req.method=='POST':
        name=req.POST['moviename']
        mhero=req.POST['hero']
        data=Movieregister.objects.filter(id=id).update(movie_name=name,movie_hero=mhero)
        return render(req,'app/home.html')
    return render(req,'app/home.html',{})


def register(req):
    if req.method=="POST":
        name=req.POST['moviename']
        ban=req.POST['banner']
        mhero=req.POST['hero']

        data=Movieregister(movie_name=name,movie_banner=ban,movie_hero=mhero)
        data.save()
        return render(req,'app/home.html')
    return render(req,'app/register.html',{})

def userregister(req):
    if req.method=='POST':
        form=UserForm(req.POST)
        form.save()
        return render(req,'app/home.html')
    form=UserForm()
    return render(req,'app/userregister.html',{'form':form})

def userdata(req):
    info = Userregister.objects.all()
    return render(req,'app/userdata.html',{'data':info})

def uedit(req,id):
    data=Userregister.objects.get(id=id)
    if req.method=="POST":
        form=UserForm(req.POST,instance=data)
        form.save()
        return HttpResponse("Data Succesfully added")

    form=UserForm(instance=data)
    return render(req,'app/uedit.html',{"form":form,"data":data})

def udelete(req,id):
    data=Userregister.objects.get(id=id)
    data.delete()
    return redirect('/tollywood/userdata/')