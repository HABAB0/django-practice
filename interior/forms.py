from django import forms
from django.contrib.auth.forms import UserCreationForm

from interior.models import User


class RegistrationForm(UserCreationForm):
    user_required_data = forms.BooleanField(required=True, help_text='I agree to the processing of personal data')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'user_required_data')