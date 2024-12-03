from django import forms
from store.models import OTP

class MobileForm(forms.Form):
    mobile_number = forms.CharField(
        max_length=15,
        label="شماره موبایل",
        widget=forms.TextInput(attrs={'placeholder': 'شماره موبایل خود را وارد کنید'})
    )


class OTPForm(forms.Form):
    otp_code = forms.CharField(
        max_length=6,
        label="رمز یکبار مصرف",
        widget=forms.TextInput(attrs={'placeholder': 'رمز یکبار مصرف'})
    )