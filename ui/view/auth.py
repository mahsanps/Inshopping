from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from ui.forms.auth import SignUpForm, LogInForm
from django.contrib.auth.models import User
from authuser.models import Account
from django.contrib.auth import logout
from django.shortcuts import redirect
from utils.views import BaseView, BaseLoginRequiredView

from django.urls import reverse


class SignUpView(BaseView):
    template_name = "signup.html"

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user: Account = form.save()
            user.set_password(form.cleaned_data["password"])
            user.save()
            user = authenticate(username=user.username, password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')  # دریافت پارامتر next
                return redirect(next_url if next_url else '/') 
        return render(request, self.template_name, {"form": form})


class SignInView(BaseView):
    template_name = "signin.html"

    def get(self, request, *args, **kwargs):
        form = LogInForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')  # دریافت پارامتر next
                return redirect(next_url if next_url else '/') 
            else:
                form.add_error(None, "شناسه نامعتبر است. لطفا دوباره سعی کنید")
        return render(request, self.template_name, {"form": form})


class LogOutView(BaseView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")
    
    
class accountInfoView(BaseView):
    def get(self, request, *args, **kwargs):
        
    
        return render(request, 'accountinfo.html',)
       
    
        
 