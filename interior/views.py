from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import *

from interior.models import User


def index(request):
    num_users = User.objects.count()

    context = {'num_users': num_users}

    return render(request, 'interior/index.html', context)