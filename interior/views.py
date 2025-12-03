from lib2to3.fixes.fix_input import context

from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import DeleteView

from .forms import RegistrationForm, CreateApplicationForm
from .models import User, Application
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'interior/registration.html', context = {'form': form})


def createApplication(request):
    if request.method == 'POST':
        form = CreateApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.author = request.user
            application.save()
            return redirect('/')
    else:
        form = CreateApplicationForm()

    return render(request, 'interior/application-create.html', context={'form': form})

class ApplicationList(LoginRequiredMixin, generic.ListView):
    model = Application
    template_name = 'interior/applications.html'


class ApplicationDelete(LoginRequiredMixin, DeleteView):
    model = Application
    template_name = 'interior/applications-delete.html'

    def form_valid(self, form):
        try:
            self.object.delete()
            return redirect('applicationList')
        except Exception as e:
            return redirect(
                reverse("applicationDelete", kwargs={"pk": self.object.pk})
            )

