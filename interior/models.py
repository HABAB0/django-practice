from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    fio = models.CharField(max_length=100 , blank=False, null=False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])


