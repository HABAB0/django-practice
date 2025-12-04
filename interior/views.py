from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import DeleteView

from interiordesign.asgi import application
from .forms import RegistrationForm, CreateApplicationForm
from .models import User, Application
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse, reverse_lazy


class Index(generic.ListView):
    model = Application
    template_name = 'index.html'
    context_object_name = 'application_list'

    def get_queryset(self):
        return ({
            'app': Application.objects.filter(status='В')[:4],
            'counter': Application.objects.filter(status='П').count()
        })

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'interior/registration.html', context={'form': form})

@login_required
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
    def get_queryset(self):
        if 'new' in self.request.GET:
            return Application.objects.filter(author=self.request.user, status='Н')
        elif 'in_work' in self.request.GET:
            return Application.objects.filter(author=self.request.user, status='П')
        elif 'complete' in self.request.GET:
            return Application.objects.filter(author=self.request.user, status='В')
        elif 'all' in self.request.GET:
            return Application.objects.filter(author=self.request.user)
        else:
            return Application.objects.filter(author=self.request.user)


class AllApplications(LoginRequiredMixin, generic.ListView):
    model = Application
    template_name = 'interior/applications-all.html'

class ApplicationUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Application
    template_name = 'interior/application-update.html'
    fields = ['status', 'category']
    success_url = reverse_lazy('applicationList')


class ApplicationDelete(LoginRequiredMixin, DeleteView):
    model = Application
    template_name = 'interior/applications-delete.html'


    def form_valid(self, form):
        try:
            if not self.request.user == self.object.author:
                return HttpResponseForbidden('Нет прав')

            self.object.delete()
            return redirect('applicationList')
        except Exception as e:
            return redirect(
                reverse("applicationDelete", kwargs={"pk": self.object.pk})
            )