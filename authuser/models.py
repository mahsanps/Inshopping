from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    class Meta:
        swappable = "AUTH_USER_MODEL" 
        verbose_name = "Account"
        verbose_name_plural = "Accounts"