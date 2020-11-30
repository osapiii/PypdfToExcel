from django.shortcuts import render


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from .forms import LoginForm

class Login(LoginView):
    """Login page"""
    form_class = LoginForm
    template_name = 'accounts/login.html'

class Logout(LoginRequiredMixin,LogoutView):
    """Logout page"""
    template_naem = 'accounts/login.html'
