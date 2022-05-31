from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
def index(request):
    return HttpResponse("Hee")


def LoginPage(request):
    if(request.method=="POST"):
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
           messages.info(request,"Username or password incorrect")             
     
    return render(request,"LoginPage.html")

def Logout(request):
    logout(request)
    return redirect("/login")