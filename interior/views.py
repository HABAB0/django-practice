from lib2to3.fixes.fix_input import context

from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .forms import RegistrationForm
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

def index(request):
    return render(request, 'index.html')

class Profile(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'interior/profile.html'


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'interior/registration.html', context = {'form': form})

