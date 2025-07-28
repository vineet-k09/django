from django.shortcuts import render 

def RegisterPage(request):
    return render(request,"register.html")