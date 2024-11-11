from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)  # اضافه کردن فیلد شماره موبایل


    class Meta:
        swappable = "AUTH_USER_MODEL" 
        verbose_name = "Account"
        verbose_name_plural = "Accounts"