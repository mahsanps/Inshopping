# views.py

from django.shortcuts import render, redirect , get_object_or_404
from store.models import Shop, Category , SubCategory, ShopImage
from ui.forms.shop import ShopForm
from utils.views import BaseView
from django.http import HttpResponse
from django.urls import reverse
from ui.forms.shopimages import ShopImagesForm

class CreateShop(BaseView):
    def get(self, request, *args, **kwargs):
        form = ShopForm()
        shop_instance = Shop.objects.filter(account=request.user)
        if self.request.htmx:
           return render(request, 'createshop.html', {'form': form,'shop_instance':shop_instance}) 
        return render(request, 'createshop_full.html', {'form': form, 'shop_instance':shop_instance}) 
            
        
    
    def post(self, request, *args, **kwargs):
      
        form = ShopForm(data=request.POST, files=request.FILES)
        shop_instance = Shop.objects.filter(account=request.user)
        if form.is_valid():
           
            shop = form.save(commit=False)
            shop.account = request.user
            shop.save()
            if self.request.htmx:
               
                return HttpResponse(status=204)
            return redirect('shop-images',pk=shop.pk)
        
        if self.request.htmx:
         
            return render(request, 'createshop.html', {'form': form, 'shop_instance': shop_instance})
       
        return render(request, 'createshop_full.html', {'form': form, 'shop_instance': shop_instance})




class EditShop(BaseView):
    def get(self, request,pk, *args, **kwargs):
        shop_instance = get_object_or_404(Shop, pk=pk)
        form = ShopForm(instance=shop_instance)
        if self.request.htmx:
            return render(request, 'editshop.html', {'form': form, 'shop_instance': shop_instance})
        return render(request, 'editshop_full.html', {'form': form, 'shop_instance': shop_instance})

    def post(self, request,pk, *args, **kwargs):
        shop_instance = get_object_or_404(Shop, pk=pk)
        form = ShopForm(request.POST,  request.FILES, instance=shop_instance)
        
        if form.is_valid():
            form.save()
            if self.request.htmx:
               
                return HttpResponse(status=204)
            return redirect('account-info')
        
        else:
            if self.request.htmx:
         
             return render(request, 'editshop.html', {'form': form, 'shop_instance': shop_instance})
       
        return render(request, 'editshop_full.html', {'form': form, 'shop_instance': shop_instance})


       
class ShopImages(BaseView):
    def get(self, request,pk, *args, **kwargs):
        shop = get_object_or_404(Shop, pk=pk)
        shop_instance = Shop.objects.filter(account=request.user).first()
        form=ShopImagesForm()
        if self.request.htmx:
           return render(request, 'shop-images.html' , {'shop_instance':shop_instance,'shop':shop,'form':form})  
        return render(request, 'shop-images-full.html' , {'shop_instance':shop_instance,'shop':shop,'form':form})       

    def post(self, request,pk, *args, **kwargs):
        shop = get_object_or_404(Shop, pk=pk)
        form = ShopImagesForm(request.POST, request.FILES)  # داده‌ها و فایل‌ها را به فرم ارسال کنید

        if form.is_valid():
            shop_image = form.save(commit=False)
            shop_image.shop = shop  # رابطه ForeignKey را تنظیم کنید
            shop_image.save() 
            return redirect('account-info')
        return render(request, 'shop-images.html', {'shop':shop,'form':form})
    
    

class ShopImagesEdit(BaseView):
    def get(self, request, pk, *args, **kwargs):
        shop = get_object_or_404(Shop, pk=pk)
        shop_instance = Shop.objects.filter(account=request.user).first()
        shop_image = get_object_or_404(ShopImage, shop__pk=pk)
        form = ShopImagesForm(instance=shop_image)

        return render(
            request, 'edit-shop-images.html',
            {'shop_instance': shop_instance, 'shop': shop, 'form': form}
        )

    
    def post(self, request, pk, *args, **kwargs):
        shop = get_object_or_404(Shop, pk=pk)
        # پیدا کردن رکورد موجود برای تصاویر فروشگاه
        shop_image = get_object_or_404(ShopImage, shop__pk=pk)

        # استفاده از instance در فرم
        form = ShopImagesForm(request.POST, request.FILES, instance=shop_image)

        if form.is_valid():
            shop_image = form.save(commit=False)
            shop_image.shop = shop
            shop_image.save()
            
            return redirect('account-info')

        return render(
            request, 'edit-shop-images.html',
            {
                'shop': shop,
                'form': form,
                'shop_image': shop_image,
            }
        )
