
from django.shortcuts import render, redirect , get_object_or_404
from store.models import Shop, Category , SubCategory , Product , ProductVariation
from utils.views import BaseView
from authuser.models import Account
from django.contrib.auth import get_user_model


User = get_user_model()

class StorePage(BaseView):        
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            username = request.user.username
            store_account = get_object_or_404(User, username=username)
        else:
            username = None
            store_account = None
            
        categories = Category.objects.all() 
        store_name = kwargs.get("store_name")
        shop_instance = get_object_or_404(Shop, store_name=store_name)
        shop_list = Shop.objects.filter(store_name=store_name)
        products = Product.objects.filter(shop__in=shop_list, is_approved=True).distinct()
        
        available_products = set()
        for product in products:
            if any(variation.quantity >= 1 for variation in product.variations.all()):
                available_products.add(product.id)
        
       
        context = {
            'shop_instance': shop_instance, 
            'store_name': store_name, 
            'categories': categories, 
            'shop_list': shop_list, 
            'store_account': store_account, 
            'username': username, 
            'products': products,
            'available_products': available_products,
        }

        return render(request, 'storepage.html', context)