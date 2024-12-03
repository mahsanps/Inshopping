# views.py

from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, ProductVariation, ProductImage, SubCategory, Category, Color, ShopAuth, Shop
from ui.forms.products import ProductsForm
from ui.forms.deleteproduct import DeleteProductForm
from utils.views import BaseView
from ui.forms.productQuantity import ProductsQuantityForm
from django.contrib.auth import get_user_model
from ui.forms.productimage import ProductsImagesForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from dal import autocomplete
from django.urls import reverse
from constants import COLOR_MAP 
from django.core.paginator import Paginator
import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
import json
import jdatetime
from datetime import datetime, timedelta

from django.utils.timezone import now as django_now  # Use Django's timezone-aware `now`
from django.utils.timezone import now as timezone_now, make_aware, is_naive



User = get_user_model()

class ProductsView(BaseView):
    def get(self, request, *args, **kwargs):
        form = ProductsForm()
        categories = Category.objects.all()
        shop_instance = Shop.objects.filter(account=request.user).first()
        if self.request.htmx:
           return render(request, 'products.html', {'shop_instance':shop_instance, 'form': form, 'categories': categories})
        return render(request, 'products-full.html', {'shop_instance':shop_instance, 'form': form, 'categories': categories})
    
    def post(self, request, *args, **kwargs):
        form = ProductsForm(request.POST, request.FILES)
       

        if form.is_valid():
            product = form.save(commit=False)
            product.shop = request.user.shop_set.first()
            product.save()

           
            return redirect(reverse('products_images', kwargs={'product_pk': product.pk}))

        return render(request, 'products.html', {'form': form})

class ProductsImages(BaseView):
    def get(self, request, product_pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_pk)
        form = ProductsImagesForm()
        return render (request, 'products-images.html',{'form':form, 'product':product})  
    
    
    def post (self, request, product_pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_pk)
        form = ProductsImagesForm(request.POST, request.FILES)
        
        if form.is_valid():
        # Check for uploaded images
           images = request.FILES.getlist('images')  # Assuming 'images' is the input field name
           if not images:
              form.add_error(None, "Please upload at least one image.")
           else:
            for image in images:
                # Create ProductImage instance for each file
                ProductImage.objects.create(product=product, image=image)
            return redirect(reverse('products_quantity', kwargs={'product_pk': product.pk}))
    
           
        return render (request, 'products-images.html', {'form':form, 'product':product})
    


class EditProductsImages(BaseView):
    def get(self, request, product_pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_pk)
        images = ProductImage.objects.filter(product=product)
        form = ProductsImagesForm()
        shop_instance = Shop.objects.filter(account=request.user).first()
        if self.request.htmx:
          return render(request, 'edit-product-images.html', {'shop_instance':shop_instance,'form': form,'product': product,'images': images})
        return render(request, 'edit-product-images-full.html', {'shop_instance':shop_instance,'form': form,'product': product,'images': images})

    def post(self, request, product_pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_pk)
        action = request.POST.get('action')

        if action == "add":
            form = ProductsImagesForm(request.POST, request.FILES)
            if form.is_valid():
                for image in request.FILES.getlist('images'):
                    ProductImage.objects.create(product=product, image=image)
                if request.htmx:
                    return redirect(reverse('edit-products-images', kwargs={'product_pk': product.pk}))
        
        elif action == "delete":
            image_ids = request.POST.getlist('image_ids')
            if image_ids:
                ProductImage.objects.filter(id__in=image_ids).delete()
                if request.htmx:
                    return redirect(reverse('edit-products-images', kwargs={'product_pk': product.pk}))

        form = ProductsImagesForm()
        return render(request, 'edit-product-images.html', {
            'form': form,
            'product': product,
            'images': ProductImage.objects.filter(product=product)
        })

    def render_images_partial(self, request, product):
        images = ProductImage.objects.filter(product=product)
        form = ProductsImagesForm()
        return render(request, 'partials/product-images.html', {
            'form': form,
            'product': product,
            'images': images
        })



class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return SubCategory.objects.none()
        
        category_id = self.forwarded.get('category', None)
        
        if category_id:
            return SubCategory.objects.filter(categoryname_id=category_id)
        return SubCategory.objects.none()
  
def load_subcategories(request):
    category_id = request.GET.get('category_id')

    if category_id:
        subcategories = SubCategory.objects.filter(categoryname_id=category_id).order_by('subname')
    else:
        subcategories = SubCategory.objects.none()

    subcategory_list = [{"id": subcategory.id, "name": subcategory.subname} for subcategory in subcategories]

    return JsonResponse({"subcategories": subcategory_list})
    
    
class ProductsListView(BaseView):
    def get(self, request, *args, **kwargs):
        shop_instance = Shop.objects.filter(account=request.user).first()
        products= Product.objects.all()
        product_list = Product.objects.filter(is_ready=True,shop__account=request.user).distinct()
        
        if 'category' in request.GET:
            category=request.GET['category']
            products=products.filter(category_id=request.GET['category'])
            
        if self.request.htmx:
            return render(request, 'productslist.html', {'shop_instance':shop_instance,'products':products,'product_list': product_list,})
        return render(request, 'productslist_full.html', {'shop_instance':shop_instance,'products':products,'product_list': product_list,})    
        
       


class SubcategoryProducts(BaseView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        subcategory_slug = kwargs.get("subcategory_slug")
        
        # Get the subcategory using the slug
        subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
        
        # Fetch all products in this subcategory
        subcategory_products = Product.objects.filter(subcategory=subcategory)

        # Fetch available colors from products
        colors = Color.objects.exclude(color__isnull=True).exclude(color="")

        color_data = []
        for color in colors:
            color_name = color.color  # Persian color name from the database
            color_code = COLOR_MAP.get(color_name, '#ffffff')  # Default to white if no match
            color_data.append({'name': color_name, 'code': color_code})

        # Fetch available sizes from products
        sizes = subcategory_products.values_list('variations__size', flat=True).exclude(variations__size__isnull=True).exclude(variations__size="").distinct()

        # Get filter parameters from the request
        selected_color = request.GET.get("color")
        selected_size = request.GET.get("size")
        price_min = request.GET.get("price_min")
        price_max = request.GET.get("price_max")

        # Apply color filter
        if selected_color and selected_color != "None" and selected_color != "":
            subcategory_products = subcategory_products.filter(variations__color__color=selected_color)

        # Apply size filter
        if selected_size and selected_size != "":
            subcategory_products = subcategory_products.filter(variations__size=selected_size)

        # Apply price filters
        if price_min:
            try:
                price_min = int(price_min)
                subcategory_products = subcategory_products.filter(price__gte=price_min)
            except ValueError:
                price_min = None

        if price_max:
            try:
                price_max = int(price_max)
                subcategory_products = subcategory_products.filter(price__lte=price_max)
            except ValueError:
                price_max = None

        # Apply pagination after filtering
        paginator = Paginator(subcategory_products, 40)  # Show 40 products per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Render the subcategory page
        return render(request, 'subcategory.html', {
            'categories': categories,
            'colors': color_data,
            'sizes': sizes,
            'page_obj': page_obj,
            'selected_color': selected_color,
            'selected_size': selected_size,
            'price_min': price_min,
            'price_max': price_max,
            'subcategory_products': subcategory_products,
            'subcategory': subcategory
        })
 
        
class ProductDetails(BaseView):
    def get(self, request, *args, **kwargs):
        product_pk: str = kwargs["product_pk"]
        product_list = Product.objects.filter(shop__account=request.user)
        product_details=get_object_or_404(Product, pk=product_pk)
        product_variation=ProductVariation.objects.filter(product__pk=product_pk)
        shop_instance = Shop.objects.filter(account=request.user).first()
        if self.request.htmx:
           return render(request, 'productdetails.html', {'shop_instance':shop_instance,'product_pk': product_pk, 'product_details':product_details, 'product_variation':product_variation, 'product_list': product_list})
        return render(request, 'productdetails-full.html', {'shop_instance':shop_instance,'product_pk': product_pk, 'product_details':product_details, 'product_variation':product_variation, 'product_list': product_list})
        
    

class EditProductView(BaseView):
    def get(self, request, product_pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_pk)
        product_form = ProductsForm(instance=product)

        # Remove fields from the form
        fields_to_remove = ['category', 'subcategory']
        for field in fields_to_remove:
            if field in product_form.fields:
                del product_form.fields[field]
        shop_instance = Shop.objects.filter(account=request.user).first()
        if self.request.htmx:
           return render(request, 'editproduct.html', {'shop_instance':shop_instance,'product_form': product_form, 'product': product})
        return render(request, 'editproduct-full.html', {'shop_instance':shop_instance,'product_form': product_form, 'product': product})
       

    def post(self, request, product_pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_pk)
        product_form = ProductsForm(request.POST, request.FILES, instance=product)

        # Remove fields from the form
        fields_to_remove = ['category', 'subcategory']
        for field in fields_to_remove:
            if field in product_form.fields:
                del product_form.fields[field]

        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.save()
            
            return redirect('product_details', product_pk=product_pk)

        return render(request, 'editproduct.html', {'product_form': product_form, })

    

class DeleteProduct(BaseView):
    def post(self, request, product_pk):
        product = get_object_or_404(Product, pk=product_pk)
        if request.method == 'POST':
            form = DeleteProductForm(request.POST, instance=product)
            if form.is_valid():
                product.delete()
                  # Redirect to your products list view
        return redirect('products_list') 
    
    
class PublishProductInstagramPost(BaseView):
    def get(self, request, product_pk):
        product = get_object_or_404(Product, pk=product_pk)
        
        product.publish_to_instagram()
        return redirect('products_list') 
    
    
