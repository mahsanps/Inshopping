
from django.shortcuts import render, redirect , get_object_or_404
from store.models import Shop, Category , SubCategory , Product , ProductVariation,Color
from utils.views import BaseView
from authuser.models import Account
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from constants import COLOR_MAP 

User = get_user_model()

class StorePage(BaseView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            username = request.user.username
            store_account = get_object_or_404(User, username=username)
        else:
            username = None
            store_account = None

        # Fetch all categories and products for the current shop
        categories = Category.objects.all()
        store_name = kwargs.get("store_name")
        shop_instance = get_object_or_404(Shop, store_name=store_name)
        shop_list = Shop.objects.filter(store_name=store_name)

        # Start with all approved products for the shop
        products = Product.objects.filter(shop__in=shop_list, is_approved=True).distinct()
        paginator = Paginator(products, 40)  # Show 10 products per page

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        # Get only products with available variations (quantity >= 1)
        available_products = set()
        for product in products:
            variations = product.variations.all()
            if any(variation.quantity >= 1 for variation in variations):
                available_products.add(product.id)

        # Fetch all available colors from your Color model
        colors = Color.objects.exclude(color__isnull=True).exclude(color="")

        color_data = []
        for color in colors:
            color_name = color.color  # Persian color name from the database
            color_code = COLOR_MAP.get(color_name, '#ffffff')  # Default to white if no match
            color_data.append({'name': color_name, 'code': color_code})

        # Fetch available sizes from products
        sizes = products.values_list('variations__size', flat=True).exclude(variations__size__isnull=True).exclude(variations__size="").distinct()

       

        subcategories = SubCategory.objects.all()

        # Get filter parameters from the request
        selected_color = request.GET.get("color")
        selected_size = request.GET.get("size")
       
        price_min = request.GET.get("price_min")
        price_max = request.GET.get("price_max")
     

        selected_subcategory = request.GET.get("subcategory")

      
        

        # Apply color filter
        if selected_color and selected_color != "None" and selected_color != "":
    # Apply color filter only if a valid color is selected
           page_obj = products.filter(variations__color__color=selected_color)
      

        # Apply size filter, only if selected_size is valid (not None or empty string)
        if selected_size and selected_size != "":
          
           page_obj = products.filter(variations__size=selected_size)
         

        # Apply price filters
        if price_min:
            try:
                price_min = int(price_min)
                page_obj = products.filter(price__gte=price_min)
            except ValueError:
                price_min = None

        if price_max:
            try:
                price_max = int(price_max)
                page_obj = products.filter(price__lte=price_max)
            except ValueError:
                price_max = None
                # Apply subcategory filter
        if selected_subcategory and selected_subcategory != "":
                page_obj = products.filter(subcategory__subname=selected_subcategory)
           

        
        

    

        context = {
            'available_products': available_products,
            'shop_instance': shop_instance,
            'store_name': store_name,
            'categories': categories,
            'shop_list': shop_list,
            'store_account': store_account,
            'username': username,
            'products': products,
            'colors': color_data,
            'sizes': sizes,
            'subcategories': subcategories,
            'selected_color': selected_color,
            'selected_size': selected_size,
            'price_min': price_min,
            'price_max': price_max,
            'selected_subcategory': selected_subcategory,
            'page_obj':page_obj,
        }

        return render(request, 'storepage.html', context)


    
class aboutShop(BaseView): 
    def get(self, request, store_name):
       
        categories = Category.objects.all() 
        shop_instance = get_object_or_404(Shop, store_name=store_name)
        shop_list = Shop.objects.filter(store_name=store_name)    
        
       
      

        return render(request, 'aboutshop.html', { 'shop_instance': shop_instance, 
            'store_name': store_name, 
            'categories': categories, 
            'shop_list': shop_list, 
           })