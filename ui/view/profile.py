from django.contrib.auth import logout
from django.shortcuts import redirect
from utils.views import BaseView
from django.shortcuts import render, redirect
from store.models import Shop


class ProfileView(BaseView):
    template_name = "profile.html"
    
    def get(self, request, *args, **kwargs):
        shop_instance = Shop.objects.filter(account=request.user).first()
        return render(request, self.template_name, {'shop_instance':shop_instance})   
    
    
class AboutUs(BaseView):
     def get(self, request, *args, **kwargs):
        shop_instance = Shop.objects.filter(account=request.user).first()
        
        if self.request.htmx:
            return render(request, 'account-info.html', {'shop_instance':shop_instance, })
        return render(request, 'accountinfo_full.html', {'shop_instance':shop_instance, })  
    


class ProductsSection(BaseView):
    def get(self,request, *args, **kwargs):
        shop_instance = Shop.objects.filter(account=request.user).first()
        if self.request.htmx:
           return render(request,'productssection.html', {'shop_instance':shop_instance}) 
        return render(request,'productsection_full.html', {'shop_instance':shop_instance}) 
            
            
class Contact(BaseView):
    def get(self,request, *args, **kwargs):
        shop_instance = Shop.objects.filter(account=request.user)
        return render(request,'contact.html', {'shop_instance':shop_instance})  
                    