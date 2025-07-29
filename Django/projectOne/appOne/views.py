from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .forms import ContactForm, RegisterForm, LoginForm
from .models import TaskBoard
from .serializers import TaskSerializer
from rest_framework import viewsets

def RegisterPage(request):
    form = RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration Complete - head to Login')
            return redirect('loginPage')
        else:
            messages.warning(request,'yeah not registered')
    return render(request,"register.html",{'form':form})

def HomePageContent(request):
    return render(request,"base.html")

def HomePage(request):
    return render(request,"homepage.html")

def DashBoardPage(request):
    return render(request,'dashboard.html')

def ContactPage(request):
    message=''
    if request.method=='POST':
        f=ContactForm(request.POST)
        if f.is_valid():
            print("Your response is recorded")
        else:
            print("Your Request is failed")
            return render(request,'contact.html',{'form':f})
    else:
        f=ContactForm()
    return render(request,'contact.html',{"form":f, 'message':message})

def LoginPage(request):
    form=LoginForm(request.POST)
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(request, username=un,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request, 'Login Succesful')
                return redirect('dashboardPage')
            else:
                messages.warning(request, 'Login UnSuccesful')
                return render(request,'login.html',{'form':form})  
        else:
            return render(request,'login.html',{'form':form})
    return render(request, 'login.html', {'form':form})

def PricingPage(request):
    
    items = [
        {
            "title": "Personal",
            "desc": "For individuals and small teams looking to manage their tasks.",
            "price": "US$0",
            "original": None,
            "features": ["Unlimited tasks", "Basic search filters", "List view projects", "Personal to-dos"]
        },
        {
            "title": "Starter",
            "desc": "For growing teams that need to track their projects' progress and hit deadlines.",
            "price": "US$6.92",
            "original": "US$10.99",
            "features": ["Unlimited tasks", "Advanced filters", "Board view", "Team collaboration"]
        },
        {
            "title": "Advanced",
            "desc": "For companies that need to manage a portfolio of work and goals across departments.",
            "price": "US$15.74",
            "original": "US$24.99",
            "features": ["Unlimited tasks", "Custom dashboards", "Priority support", "Integrations"]
        },
    ]
    return render(request,"pricing.html",{"items":items})

class TaskView(viewsets.ModelViewSet):
    queryset = TaskBoard.objects.all()
    serializer_class = TaskSerializer

def LogOutPage(request):
    logout(request)
    return redirect('loginPage')