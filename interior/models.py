from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    fio = models.CharField(max_length=100 , blank=False, null=False)

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

class Application(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/')

    APPLICATION_STATUS = (
        ('Н', 'Новая'),
        ('П', 'Принято в работу'),
        ('В', 'Выполнено'),
    )

    status = models.CharField(max_length=1, choices=APPLICATION_STATUS, blank=True, default='Н')
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    comment = models.TextField(blank=True, null=True)
    design_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('applicationList', args=[str(self.id)])


class Category(models.Model):
    category = models.CharField( blank=True)

    def __str__(self):
        return self.category