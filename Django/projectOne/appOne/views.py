from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .forms import ContactForm, RegisterForm, LoginForm

def RegisterPage(request):
    form = RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            messages.success(request, 'Registration Complete - head to Login')
            return redirect('loginPage')
    return render(request,"register.html",{'form':form})

def HomePage(request):
    return render(request,"base.html")

def HomePageContent(request):
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
                messages.success(request, 'Registration Complete - head to Login')
                return redirect('dashboardPage')
            else:
              return redirect('loginPage')    
        else:
            return render(request,'login.html',{'form':form})
    return render(request, 'login.html', {'form':form})

def PricingPage(request):
    return render(request,"pricing.html")


items=[
    {"title":"Personal", "des":"For individuals and small teams looking to manage their tasks.", },
    {"title":"Starter"},
    {"title":"Advanced"}
]

users=[
    {"name":"Eeksha", "age": 21},
    {"name":"Prajwal", "age": 56},
    {"name":"ABC", "age": 30}
]

def LogOutPage(request):
    logout(request)
    return redirect('loginPage')