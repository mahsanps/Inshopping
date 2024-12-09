from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from authuser.models import Account 
from django.utils.translation import gettext_lazy as _



class SignUpForm(forms.ModelForm):
    firstname= forms.CharField(max_length=300,label=' نام')
    lastname= forms.CharField(max_length=300,label='نام خانوادگی')
    email = forms.EmailField(label='ایمیل')
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
    phone= forms.CharField(max_length=300, label='شماره موبایل')
    
   

    class Meta:
        model = Account
        fields = ('username', 'email', 'password','firstname','lastname','phone')


class LogInForm(forms.Form):
    username = forms.CharField(label='نام کاربری')
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
    
    

       