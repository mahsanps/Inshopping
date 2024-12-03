from django.shortcuts import render, redirect, get_object_or_404
from utils.views import BaseView
from ui.forms.bankaccount import BankAccountForm
from store.models import BankAccount, Shop, Order, OrderItem
from django.contrib.auth import get_user_model


user = get_user_model()

class WalletView(BaseView):
    def get(self, request, *args, **kwargs):
        shop = request.user.shop_set.first()
        bankaccount = BankAccount.objects.filter(shop=shop).distinct()
        orders_registered=OrderItem.objects.filter(variation__product__shop=shop)
        total_price = sum(item.variation.product.price * item.quantity for item in orders_registered)
    
        return render(request, 'wallet.html', {"bankaccount": bankaccount, 'orders_registered': orders_registered,'total_price':total_price})

class BankAccountView(BaseView):
    def get(self, request, *args, **kwargs):
        form= BankAccountForm()
        shop_instance = Shop.objects.filter(account=request.user).first()
        if self.request.htmx:
           return render (request, 'bankaccount.html', {'shop_instance':shop_instance,"form":form})
        return render (request, 'bankaccount-full.html', {'shop_instance':shop_instance,"form":form})
    
    def post(self, request, *args, **kwargs):
        form= BankAccountForm(request.POST)
        if form.is_valid():
            shop = request.user.shop_set.first()
            bankaccount = form.save(commit=False)
            bankaccount.shop = shop
            bankaccount.save()
            return (redirect('mywallet'))
        return render (request, 'bankaccount.html', {"form":form})
    
    
class EditBankAccount(BaseView):
    def get(self, request,pk, *args, **kwargs):
        bankaccount = get_object_or_404(BankAccount, pk=pk)
        form = BankAccountForm(instance=bankaccount)
        return render(request, 'editbankaccount.html', {'form': form, 'bankaccount': bankaccount})

    def post(self, request,pk, *args, **kwargs):
        bankaccount = get_object_or_404(BankAccount, pk=pk)
        form = BankAccountForm(request.POST, instance=bankaccount)
        if form.is_valid():
            form.save()
            return redirect('mywallet')
        return render(request, 'editbankaccount.html', {'form': form, 'bankaccount': bankaccount})    
    
  