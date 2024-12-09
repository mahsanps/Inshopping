from django import forms
from store.models import OTP

class MobileForm(forms.Form):
    mobile_number = forms.CharField(
        max_length=15,
        label="شماره موبایل",
        widget=forms.TextInput()
    )


class OTPForm(forms.Form):
    otp_code = forms.CharField(
        max_length=6,
        label="کد تایید",
        widget=forms.TextInput()
    )