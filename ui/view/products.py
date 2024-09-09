# views.py

from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, ProductVariation, ProductImage, SubCategory, Category
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


User = get_user_model()

class ProductsView(BaseView):
    def get(self, request, *args, **kwargs):
        form = ProductsForm()
        categories = Category.objects.all()
        return render(request, 'products.html', {'form': form, 'categories': categories})
    
    def post(self, request, *args, **kwargs):
        form = ProductsForm(request.POST, request.FILES)
        image_form = ProductsImagesForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.shop = request.user.shop_set.first()
            product.save()
            for image in request.FILES.getlist('image'):
                product_image = ProductImage(product=product, image=image)
                product_image.save()
                
                images = request.FILES.getlist('images')
            for image in images:
                ProductImage.objects.create(product=product, image=image)
                
                
            print(f"Product PK: {product.pk}")    
            return redirect(reverse('products_quantity', kwargs={'product_pk':product.pk}))
        return render(request, 'products.html', {'form': form })


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return SubCategory.objects.none()
        
        category_id = self.forwarded.get('category', None)
        print("Forwarded category ID:", category_id)
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
        products= Product.objects.all()
        product_list = Product.objects.filter(shop__account=request.user).distinct()
        
        if 'category' in request.GET:
            category=request.GET['category']
            products=products.filter(category_id=request.GET['category'])
        
        return render(request, 'productslist.html', {'products':products,'product_list': product_list,})


class SubcategoryProducts(BaseView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        subname: str= kwargs["subname"]
        subcategory=SubCategory.objects.get(subname=subname)
        subcategory_products= Product.objects.filter(subcategory=subcategory)
        
        return render(request, 'subcategory.html', {'subname':subname,'categories':categories,'subcategory_products':subcategory_products,'subcategory':subcategory})    
        
class ProductDetails(BaseView):
    def get(self, request, *args, **kwargs):
        product_pk: str = kwargs["product_pk"]
        product_list = Product.objects.filter(shop__account=request.user)
        product_details=get_object_or_404(Product, pk=product_pk)
        product_variation=ProductVariation.objects.filter(product__pk=product_pk)
        return render(request, 'productdetails.html', {'product_pk': product_pk, 'product_details':product_details, 'product_variation':product_variation, 'product_list': product_list})
    
        
    

class EditProductView(BaseView):
    def get(self, request, product_pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_pk)
        product_form = ProductsForm(instance=product)

        # Remove fields from the form
        fields_to_remove = ['category', 'subcategory']
        for field in fields_to_remove:
            if field in product_form.fields:
                del product_form.fields[field]

        return render(request, 'editproduct.html', {'product_form': product_form, 'product': product})

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
        return redirect('productssection') 
    