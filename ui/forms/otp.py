from django import forms
from store.models import OTP

class MobileForm(forms.ModelForm):
    class Meta:
        model = OTP
        fields =('mobile_number',)

class OTPForm(forms.Form):
    mobile_number = forms.CharField(max_length=15, widget=forms.HiddenInput)
    otp_code = forms.CharField(max_length=6)
