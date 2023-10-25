from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(upload_to='users/', null=True, blank=True, verbose_name='Аватар')
    phone = models.CharField(max_length=35, null=True, blank=True, verbose_name='Телефон')
    country = models.CharField(max_length=35, null=True, blank=True, verbose_name='Страна')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


