from django.shortcuts import redirect
from django.urls import reverse

class AuthRedirectMiddleware:
    def __init__(self, get_response):  
        self.get_response = get_response

    def __call__(self, request):     
        user = request.user
        path = request.path

        # Redirect authenticated users away from login/register
        if user.is_authenticated and path in [reverse('loginPage'), reverse('registerPage')]:
            return redirect('dashboardPage')

        # Redirect unauthenticated users away from protected pages
        protected_paths = [reverse('dashboardPage'), reverse('logoutPage')] 
        if not user.is_authenticated and path in protected_paths:
            return redirect('home')

        return self.get_response(request)
