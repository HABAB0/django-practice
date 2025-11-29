from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    FIO = models.CharField(max_length=100 , blank=False, null=False),
    agree_personal_data = models.BooleanField(default=False)


