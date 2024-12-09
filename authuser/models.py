from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Account(AbstractUser):
    firstname= models.CharField(max_length=300,default="", verbose_name=_("firstname"))
    lastname= models.CharField(max_length=300,default="", verbose_name=_("lastname"))
    phone = models.CharField(max_length=15, blank=True, null=True)  # اضافه کردن فیلد شماره موبایل

   
      

    class Meta:
        swappable = "AUTH_USER_MODEL" 
        verbose_name = "Account"
        verbose_name_plural = "Accounts"