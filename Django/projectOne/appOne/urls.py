# from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskView
from . import views

router = DefaultRouter()
router.register('tasks',TaskView)

urlpatterns = [
    path('register', views.RegisterPage, name="registerPage"),
    path('contact', views.ContactPage, name="contactPage"),
    path('pricing', views.PricingPage, name="pricingPage"),
    path('login', views.LoginPage, name="loginPage"),
    path('logout', views.LogOutPage, name="logoutPage"),
    path('dashboard', views.DashBoardPage, name="dashboardPage"),
    path('api/', include(router.urls)),
    path('', views.HomePage),
    path('', views.HomePageContent, name='home'),
]