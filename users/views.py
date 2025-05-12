from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

# Create your views here.
def user(request):
    return HttpResponse("Welcome to users App")

def profile(request):
    # Profile view logic
    pass

def login(request):
    # Login view logic
    pass

# In cart/views.py
def cart(request):
    # Cart view logic
    pass