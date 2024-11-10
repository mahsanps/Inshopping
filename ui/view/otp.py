from django.conf import settings
from medianasms import Client, Error, HTTPError
from django.shortcuts import render, redirect, get_object_or_404
from store.models import OTP
from datetime import timedelta
from django.utils import timezone
import random
from ui.forms.otp import MobileForm, OTPForm

# ایجاد کلاینت مدیانا
api_key = settings.MEDIANA_API_KEY
sms_client = Client(api_key)

def generate_otp():
    return random.randint(100000, 999999)

def send_otp_via_mediana(mobile_number, otp_code):
    try:
        bulk_id = sms_client.send(
            originator="+9810001",  # شماره ارسال‌کننده معتبر
            recipients=[mobile_number],
            message=f'Your OTP code is {otp_code}'
        )
        return bulk_id
    except Error as e:
        print(f"Mediana Error - Code: {e.code}, Message: {e.message}")
    except HTTPError as e:
        print(f"HTTP Error: {e}")


def send_otp_view(request):
    if request.method == 'POST':
        form = MobileForm(request.POST)
        if form.is_valid():
            mobile_number = form.cleaned_data.get('mobile_number')
            otp_code = generate_otp()
            OTP.objects.create(mobile_number=mobile_number, otp_code=otp_code)
            send_otp_via_mediana(mobile_number, otp_code)
            return redirect('verify_otp', mobile_number=mobile_number)
    else:
        form = MobileForm()
    
    return render(request, 'send_otp.html', {'form': form})

# ویو برای تایید کد OTP
def verify_otp_view(request, mobile_number):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            otp_code = form.cleaned_data.get('otp_code')
            otp_instance = get_object_or_404(OTP, mobile_number=mobile_number, otp_code=otp_code)
            if otp_instance.is_valid():
                # کد معتبر است، تایید ورود انجام شود
                return redirect('index')
            else:
                # کد منقضی شده است، پیام خطا نشان داده شود
                return render(request, 'verify_otp.html', {'form': form, 'error': 'کد منقضی شده است'})
    else:
        form = OTPForm(initial={'mobile_number': mobile_number})
    
    return render(request, 'verify_otp.html', {'form': form})