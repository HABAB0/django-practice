import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    fio = models.CharField(max_length=100 , blank=False, null=False)

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()

    CATEGORIES = (
        ('Н', 'Нормальная такая'),
        ('П', 'Пойдёт'),
        ('И', 'Идеал'),
    )

    category = models.CharField(max_length=1, choices=CATEGORIES, blank=True, default='П')
    image = models.ImageField(upload_to='images/')

    APPLICATION_STATUS = (
        ('Н', 'Новая'),
        ('П', 'Принято в работу'),
        ('В', 'Выполнено'),
    )

    status  = models.CharField(max_length=1, choices=APPLICATION_STATUS, blank=True, default='Н')
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('User', on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('application', args=[str(self.id)])