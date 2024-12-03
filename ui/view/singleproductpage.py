from django.shortcuts import render, redirect , get_object_or_404
from utils.views import BaseView
from store.models import Product, Category, ProductVariation, Color,ProductImage
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
from django.http import HttpResponseBadRequest
from django.http import JsonResponse


class SingleProductPage(BaseView):
    
    def get(self, request, store_name, *args, **kwargs):
        categories = Category.objects.all()
        product_pk = kwargs["product_pk"]
        product_details = get_object_or_404(Product, pk=product_pk)
        product_images = ProductImage.objects.filter(product__pk=product_pk)
        product_variations = list(ProductVariation.objects.filter(product__pk=product_pk).values('id', 'color__color', 'size', 'quantity'))
        
        available_products = set()
        if any(variation.quantity >= 1 for variation in product_details.variations.all()):
            available_products.add(product_details.id)
        
        colors = {variation['color__color'] for variation in product_variations if variation['color__color']}
        sizes = {variation['size'] for variation in product_variations if variation['size']}

        return render(request, 'single-product-page.html', {
            'product_details': product_details,
            'product_pk': product_pk,
            'categories': categories,
            'product_variations': json.dumps(product_variations, cls=DjangoJSONEncoder),
            'colors': colors,
            'sizes': sizes,
            "store_name": store_name,
            "available_products": available_products,
            'product_images':product_images,
        })
        
    def post(self, request,store_name, *args, **kwargs):
        product_pk = kwargs.get("product_pk")
        color_name = request.POST.get('color')
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity', 1))
        product = Product.objects.get(pk=product_pk)
        store_name = product.shop.store_name 

        cart_cookie = request.COOKIES.get("cart", "{}")
        cart_cookie_dict = json.loads(cart_cookie)
        store_cart_cookie = cart_cookie_dict.get(store_name, {})
        store_cart_items = store_cart_cookie.get("cart_items", [])

        try:
            color = Color.objects.filter(color=color_name).first() if color_name else None
            variations = ProductVariation.objects.filter(product=product)
            if color:
                variations = variations.filter(color=color)
            if size:
                variations = variations.filter(size=size)
            variation = variations.first()  
        except Color.DoesNotExist:
            return HttpResponseBadRequest("Invalid color specified.")
        
        variation_id = variation.pk if variation else None
        
        item_found = False
        for item in store_cart_items:
            if item.get("variation_id") == variation_id:
                item["quantity"] += quantity
                item_found = True
                break
        
        if not item_found:
            store_cart_items.append({
                "variation_id": variation_id,
                "price": product.price,  # Adjust as necessary
                "quantity": quantity,
                "name": product.name,
                "image": product.image.url,
                "color": color_name,
                "size": size,
                "store_name": product.shop.store_name,
            })

        store_cart_cookie["cart_items"] = store_cart_items

        response = HttpResponseRedirect(reverse("cart", kwargs={"store_name": store_name}))
        if not cart_cookie_dict.get(store_name):
            cart_cookie_dict[store_name] = {}
        cart_cookie_dict[store_name].update(store_cart_cookie)
        response.set_cookie('cart', value=json.dumps(cart_cookie_dict))
        
        return response
    
class AvailableColorsView(BaseView):
    def get(self, request, *args, **kwargs):
        product_pk = kwargs.get("product_pk")
        size = request.GET.get('size')

        if not size:
            return JsonResponse({"error": "Size is required"}, status=400)

        product_variations = ProductVariation.objects.filter(product__pk=product_pk, size=size).values('color__id', 'color__color')

        colors = [{'id': variation['color__id'], 'color': variation['color__color']} for variation in product_variations]

        return JsonResponse(colors, safe=False)