from django.shortcuts import render, get_object_or_404
from store.models import Category, Shop, Product, SubCategory, Blog
from django.shortcuts import redirect
from django.utils import translation
from django.core.paginator import Paginator
from django.conf import settings
from django.utils.translation import gettext as _

# Create your views here.
def Index_view(request):
    categories = Category.objects.all()
    shop_list = Shop.objects.filter(is_approved=True)
    products = Product.objects.filter(is_approved=True).order_by('?')[:60] 
    user = request.user
    shop_chunks = [shop_list[i:i + 10] for i in range(0, len(shop_list), 10)] 
   
    available_products = set()
    for product in products:
            if any(variation.quantity >= 1 for variation in product.variations.all()):
                available_products.add(product.id)
    
    if 'category' in request.GET:
        category_slug = request.GET.get('category')
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    
    return render(request, "index.html", {'shop_chunks': shop_chunks,'categories': categories , 'shop_list':shop_list, 'products':products, "user": user,"available_products":available_products})
    
def Terms_Conditions(request):
        
 return render(request, 'terms&conditions.html')    

def Privacy_Policy(request):
        
 return render(request, 'privacy_policy.html')  

def Contact(request):
        
 return render(request, 'contactus.html')   

def about(request):
    return render(request, 'about.html')

def blog(request):
    posts = Blog.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'blog.html', {'posts': posts})

def blog_detail(request, slug):
    post = Blog.objects.get(slug=slug, is_published=True)
    return render(request, 'blog_detail.html', {'post': post})

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
