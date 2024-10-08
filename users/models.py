from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="Email")

    avatar = models.ImageField(
        upload_to='users/photo',
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите ваше фото",
    )
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name='Номер телефона',
        help_text='Введите ваш номер',
    )
    country = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Страна',
        help_text='Укажите страну',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
