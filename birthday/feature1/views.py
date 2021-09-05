from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Birthday
import sqlite3
# Create your views here.
def index(request):
    return render(request ,'index.html')

def register(request):
    if(request.method=='POST'):
        name=request.POST['name']
        email =request.POST['email']
        password= request.POST['pass']
        repassword=request.POST['re_pass']
        if(password==repassword):
            if(User.objects.filter(email=email).exists()):
                messages.info(request,'email already used')
                return redirect('register')
            elif(User.objects.filter(username=name).exists()):
                messages.info(request, 'username already used')
                return redirect('register')
            else:
                user=User.objects.create_user(username=name,email=email,password=password)
                user.save();
                return redirect('login')
    return render(request,'register.html')

def login(request):
    if (request.method=='POST'):
        username = request.POST['username']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def data(request):
    base=sqlite3.connect('bday.db')
    curse=base.cursor()
    tuple_data=[]
    if(request.method=='POST'):
        name =request.POST['personname']
        dob=request.POST['dob']
        email=request.POST['email']
        tuple_data.append(tuple(name,dob,email))
    print(tuple_data)
    curse.execute("INSERT INTO details  FROM (?,?,?)",tuple_data)
    return render(request,'birthday.html')