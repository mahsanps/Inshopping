from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from ui.forms.auth import SignUpForm, LogInForm
from django.contrib.auth.models import User
from authuser.models import Account
from django.contrib.auth import logout
from django.shortcuts import redirect
from utils.views import BaseView, BaseLoginRequiredView
from ui.forms.auth import AccountInfoForm
from store.models import AccountInfo
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
            return redirect("/")
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
                return redirect("/")
            else:
                form.add_error(None, "Invalid credentials. Please try again.")
        return render(request, self.template_name, {"form": form})


class LogOutView(BaseView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")
    
    
class accountInfoView(BaseView):
    def get(self, request, *args, **kwargs):
        account_info = AccountInfo.objects.filter(user=request.user).first()
        if account_info:
            form = AccountInfoForm(instance=account_info)
        else:
            form = AccountInfoForm()
        
    
        return render(request, 'accountinfo.html', {'form': form, 'account_info':account_info})
       
    
        
    
    def post(self, request, *args, **kwargs):
        account_info = AccountInfo.objects.filter(user=request.user).first()
        if account_info:
            form = AccountInfoForm(request.POST, instance=account_info)
        else:
            form = AccountInfoForm(request.POST)
        
        if form.is_valid():
            account_info = form.save(commit=False)
            account_info.user = request.user
            account_info.save()
            return redirect('account-info')  # Redirect after successful save
        
        return render(request, 'accountinfo.html', {'form': form, 'account_info':account_info})   
    
    
class EditAccountInfo(BaseView):
    def get(self, request,pk, *args, **kwargs):
        account_info = get_object_or_404(AccountInfo, pk=pk)
        form = AccountInfoForm(instance=account_info)
        return render(request, 'editaccountinfo.html', {'form': form, 'account_info': account_info, 'pk': pk})

    def post(self, request,pk, *args, **kwargs):
        account_info = get_object_or_404(AccountInfo, pk=pk)
        form = AccountInfoForm(request.POST, instance=account_info)
        if form.is_valid():
            form.save()
            return redirect(reverse('account-info'))
        return render(request, 'editaccountinfo.html', {'form': form, 'account_info': account_info, 'pk': pk})
              
