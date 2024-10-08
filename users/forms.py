from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm

from users.models import User
from catalog.forms import StyleFormMixin


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class RecoveryPasswordForm(StyleFormMixin, PasswordResetForm):
    class Meta:
        model = User
        fields = ('email',)