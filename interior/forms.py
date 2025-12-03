import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from interior.models import User, Application


class RegistrationForm(UserCreationForm):
    user_required_data = forms.BooleanField(label='Согласие на обработку персоональных данных',)
    fio = forms.CharField(label='ФИО')

    def clean_fio(self):
        data = self.cleaned_data['fio']
        r = re.compile(r'[А-яЁё\-\s]+')
        if not re.fullmatch(r, data):
            raise ValidationError('Неверный формат ФИО')
        return data

    def clean_username(self):
        data = self.cleaned_data['username']
        r = re.compile(r'[A-z\-\s]+')
        if not re.fullmatch(r, data):
            raise ValidationError('Неверный формат Логина')
        return data

    class Meta:
        model = User
        fields = ('fio', 'username', 'email')


class CreateApplicationForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Application
        fields = ('name', 'description', 'category', 'image')
        author = forms.CharField(widget=forms.HiddenInput())
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'category': 'Категория',
            'image': 'Изображение'
        }
    def clean_image(self):
        data = self.cleaned_data['image']
        valid_formats = ['png', 'jpg', 'jpeg', 'bmp']
        if not data.name.endswith(valid_formats):
            raise ValidationError('Неверный формат файла')

