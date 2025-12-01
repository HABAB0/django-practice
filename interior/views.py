from lib2to3.fixes.fix_input import context
from django.shortcuts import render
from django.views.generic import CreateView

from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

def index(request):
    return render(request, 'index.html')

class Profile(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'interior/profile.html'

class Registration(CreateView):
    model = User
    fields = ['fio', 'username', 'email', 'password']
    template_name = 'interior/registration.html'