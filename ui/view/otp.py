import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import login
from ui.forms.otp import MobileForm, OTPForm
from store.models import Account, OTP
from utils.utils import send_pattern_sms  # متد ارسال پیامک

# تولید کد OTP
def generate_otp():
    return random.randint(100000, 999999)

# ویو ارسال OTP
def send_otp_view(request):
    if request.method == 'POST':
        form = MobileForm(request.POST)
        if form.is_valid():
            mobile_number = form.cleaned_data['mobile_number']

            # Check if the phone number exists
            if Account.objects.filter(phone=mobile_number).exists():
                otp_code = generate_otp()
                OTP.objects.create(mobile_number=mobile_number, otp_code=otp_code)

                # Send SMS
                response = send_pattern_sms(
                    mobile_number=mobile_number,
                    pattern_code="800128",
                    otp_code=otp_code
                )

                if response and response.status_code == 200:
                    messages.success(request, "کد تأیید ارسال شد!")
                

                return redirect('verify_otp', mobile_number=mobile_number)
            else:
                messages.error(request, "این شماره موبایل ثبت نشده است. لطفاً ابتدا ثبت‌نام کنید.")
                return redirect('signup')
    else:
        form = MobileForm()

    return render(request, 'send_otp.html', {'form': form})


# ویو تأیید OTP
def verify_otp_view(request, mobile_number):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            otp_code = form.cleaned_data['otp_code']
            otp_instance = OTP.objects.filter(mobile_number=mobile_number, otp_code=otp_code).first()

            if otp_instance and otp_instance.is_valid():
                # ورود کاربر
                user = Account.objects.get(phone=mobile_number)
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "کد تأیید نامعتبر یا منقضی شده است.")
    else:
        form = OTPForm()

    return render(request, 'verify_otp.html', {'form': form, 'mobile_number': mobile_number})
