from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from authuser.models import Account 
from store.models import AccountInfo



class SignUpForm(forms.ModelForm):
    email = forms.EmailField(label='ایمیل')
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'email', 'password')


class LogInForm(forms.Form):
    username = forms.CharField(label='نام کاربری')
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
    
    
class AccountInfoForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(),required=False)
    user = forms.ModelChoiceField(queryset=Account.objects.all(), widget=forms.HiddenInput(),required=False)
    class Meta:
        model = AccountInfo
        fields = ('firstname','lastname', 'phone')
         
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget = forms.HiddenInput()  # Set the id field widget to HiddenInput
        self.fields['id'].disabled = True 
        self.fields['firstname'].required = True
        self.fields['lastname'].required = True
        self.fields['phone'].required = True