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
    image = forms.ImageField(label='Изображение')
    class Meta:
        model = Application
        fields = ('name', 'description', 'category', 'image')
        author = forms.CharField(widget=forms.HiddenInput())
        labels = {
            'name': 'Название заявки',
            'description': 'Описание',
            'category': 'Категория',
        }
    def clean_image(self):
        data = self.cleaned_data['image']
        valid_formats = ['png', 'jpg', 'jpeg', 'bmp']
        if not data.name.split('.')[-1] in valid_formats:
            raise ValidationError('Неверный формат файла')
        if not data.size / 1024 / 1024 <= 2:
            raise ValidationError('Слишком болльшой фаил')
        return data

class EditApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('status', 'category', 'comment', 'design_image')
        labels = {
            'status': 'Статус',
            'category': 'Категория',
            'comment': 'Комментарий',
            'design_image': 'Изображение дизайна'
        }

    def clean(self):
        new_status = self.cleaned_data['status']
        comment = self.cleaned_data['comment']
        design_image = self.cleaned_data['design_image']
        current_status = self.instance.status

        if current_status in ['В', "П"] and not current_status == new_status:
            raise ValidationError('Заявка уже принята')

        if current_status in ['Н']:
            if new_status == 'П' and not comment:
                raise ValidationError('Комментарий обезателен для заполнения')

        if current_status in ['Н', 'П']:
            if new_status == 'В' and not design_image:
                raise ValidationError('Обязательно добовление дизайна')
        return self.cleaned_data