from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages,redirects
from .models import Feature

# Create your views here.
def index(request):
    return render(request,'main.html')
    
def user_reg(request):
    if request.method=='POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pw = request.POST['password']
        pwv = request.POST['password1']
        user=User.objects.Create_user(username=fname,email=email,password=pw)
        user.save();
        #return redirects('login')
    return render(request,'user_reg.html')

def user_login(request):
    if request.method=='POST':
        a=request.POST['user']

    
    return render(request,'user_login.html')


