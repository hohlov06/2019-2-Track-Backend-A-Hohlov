from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):  # AbstractUser
    # name = models.CharField(max_length=63)
    nick = models.CharField(max_length=31, blank=True, default='', verbose_name='Никнейм')
    avatar = models.CharField(max_length=2090, blank=True, default='', verbose_name='Аватар')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
