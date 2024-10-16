from tempfile import template
from tkinter.font import names

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from users.apps import UsersConfig
from users.views import email_verification, UserCreateView, RecoveryPasswordView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('password-recovery/', RecoveryPasswordView.as_view(template_name="users/password_recovery.html"), name='password-recovery')
]
