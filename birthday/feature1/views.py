from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Birthday
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
                user.save()
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

@login_required(login_url='login')
def data(request):
    day=Birthday.objects.all()
    if(request.method=='POST'):
        name =request.POST['personname']
        dob=request.POST['dob']
        email=request.POST['email']
        username=request.user.username
        if(Birthday.objects.filter(name=name).exists()):
            if (Birthday.objects.filter(email=email).exists()):
                messages.info(request,'your beloved name and data already saved')
                return redirect('/birthday')
        else:
            Birthday.objects.create(name=name,dob=dob,email=email,created_by=username)
            return redirect('/display')
    return render(request,'birthday_reg.html',{'day': day,'messages':messages})

@login_required
def display(request):
    name=request.user.username
    dataum=Birthday.objects.filter(created_by=name).all()
    context={
        'data' : dataum
    }
    return render(request,'dataum.html',context)