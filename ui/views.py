from django.shortcuts import render, get_object_or_404
from store.models import Category, Shop, Product, SubCategory
from django.shortcuts import redirect
from django.utils import translation
from django.core.paginator import Paginator
from django.conf import settings

# Create your views here.
def Index_view(request):
    categories = Category.objects.all()
    shop_list = Shop.objects.filter(is_approved=True)
    products = Product.objects.filter(is_approved=True).order_by('?')[:60] 
    user = request.user

   
    
    available_products = set()
    for product in products:
            if any(variation.quantity >= 1 for variation in product.variations.all()):
                available_products.add(product.id)
    
    if 'category' in request.GET:
            category=request.GET['category']
          
            products=products.filter(category_id=request.GET['category'])
    
    return render(request, "index.html", {'categories': categories , 'shop_list':shop_list, 'products':products, "user": user,"available_products":available_products})
    
def Terms_Conditions(request):
        
 return render(request, 'terms&conditions.html')    

def Contact(request):
        
 return render(request, 'contactus.html')   

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def guid(request):
    return render(request, 'guid.html')


def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        next_url = request.POST.get('next', '/')
        response = redirect(next_url)
        if language:
            translation.activate(language)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        return response
    return redirect('/')
