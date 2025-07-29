# from django.contrib import admin
from django.urls import path # type: ignore
# import views
from . import views

urlpatterns = [
    path('register', views.RegisterPage, name="registerPage"),
    path('contact', views.ContactPage, name="contactPage"),
    path('pricing', views.PricingPage, name="pricingPage"),
    path('login', views.LoginPage, name="loginPage"),
    path('logout', views.LogOutPage, name="logoutPage"),
    path('dashboard', views.DashBoardPage, name="dashboardPage"),
    path('', views.HomePage, name='home'),
    path('', views.HomePageContent, name='home'),
]
