# views.py

from django.shortcuts import render, redirect , get_object_or_404
from store.models import Shop, Category , SubCategory
from ui.forms.shop import ShopForm
from utils.views import BaseView
from django.http import HttpResponse
from django.urls import reverse

class CreateShop(BaseView):
    def get(self, request, *args, **kwargs):
        form = ShopForm()
        shop_instance = Shop.objects.filter(account=request.user)
        if self.request.htmx:
           return render(request, 'createshop.html', {'form': form,'shop_instance':shop_instance}) 
        return render(request, 'createshop_full.html', {'form': form, 'shop_instance':shop_instance}) 
            
        
    
    def post(self, request, *args, **kwargs):
        print("POST method called")
        form = ShopForm(data=request.POST, files=request.FILES)
        shop_instance = Shop.objects.filter(account=request.user)
        if form.is_valid():
            print("Form is valid")
            shop = form.save(commit=False)
            shop.account = request.user
            shop.save()
            if self.request.htmx:
                print("HTMX request, sending 204 No Content")
                return HttpResponse(status=204)
            return redirect('account-info')
        else:
            print("Form is invalid", form.errors)

        if self.request.htmx:
            print("HTMX request with errors")
            return render(request, 'createshop.html', {'form': form, 'shop_instance': shop_instance})
        print("Normal request with errors")
        return render(request, 'createshop_full.html', {'form': form, 'shop_instance': shop_instance})




class EditShop(BaseView):
    def get(self, request,pk, *args, **kwargs):
        shop_instance = get_object_or_404(Shop, pk=pk)
        form = ShopForm(instance=shop_instance)
        return render(request, 'editshop.html', {'form': form, 'shop_instance': shop_instance})

    def post(self, request,pk, *args, **kwargs):
        shop_instance = get_object_or_404(Shop, pk=pk)
        form = ShopForm(request.POST,  request.FILES, instance=shop_instance)
        if form.is_valid():
            form.save()
            return redirect('account-info')
        return render(request, 'editshop.html', {'form': form, 'shop_instance': shop_instance})
        
        
