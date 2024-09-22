from django.shortcuts import redirect, render, get_object_or_404
from utils.views import BaseView
import requests
from store.models import Product, Order, OrderItem, ProductVariation, Color, OrderDelivery, Category, Shop, AccountInfo
from ui.forms.orderquantity import QuantityOrderForm
from django.contrib.auth import get_user_model
from .dataclasses import Cart, CartItem
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from dataclasses import asdict
import json
from django.http import HttpResponseBadRequest
from ui.forms.ckeckout import CheckoutForm
from inshopping import settings
from django.contrib import messages
from urllib.parse import quote


user = get_user_model()




class CartView(BaseView):
    def get(self, request, store_name):
        cart_cookie = request.COOKIES.get("cart", "{}")
        cart_cookie_dict = json.loads(cart_cookie)
        store_cart_cookie = cart_cookie_dict.get(store_name, {})
        store_cart_items = []
        categories = Category.objects.all() 
        
        
        for cart_item in store_cart_cookie.get("cart_items", []):
            if cart_item.get("variation_id"):
                temp_variation = ProductVariation.objects.filter(pk=cart_item.get("variation_id")).first()
                if not temp_variation:
                    continue
                product = temp_variation.product
            else:
                product = Product.objects.filter(name=cart_item.get("name")).first()

            if product:
                store_cart_items.append(CartItem(
                product_id=product.pk,
                variation_id=cart_item.get("variation_id"), 
                price=cart_item.get("price"), 
                quantity=cart_item.get("quantity"),
                name=cart_item.get("name"),
                image=cart_item.get("image"),
                color=cart_item.get("color"),
                size=cart_item.get("size"),
                store_name=product.shop.store_name, 
               
            ))
        store_cart_cookie["cart_items"] = store_cart_items
        cart = Cart(**store_cart_cookie)        
        
        total_price = cart.get_total_price()
        return render(request,'cart.html',{'cart':cart,'total_price': total_price,'categories':categories ,"store_name": store_name})

class UpdateCartItemView(BaseView):
    def post(self, request, store_name, variation_pk):
        quantity = int(request.POST.get('quantity', 1))
        cart_cookie = request.COOKIES.get("cart", "{}")
        cart_cookie_dict = json.loads(cart_cookie)
        store_cart_cookie = cart_cookie_dict.get(store_name, {})
        store_cart_items = store_cart_cookie.get("cart_items", [])
        
        if variation_pk == 'none':
            product_name = request.POST.get('name')
            for item in store_cart_items:
                if item["variation_id"] is None and item["name"] == product_name:
                    item["quantity"] = quantity
                    break
        else:
            for item in store_cart_items:
                if item["variation_id"] == int(variation_pk):
                    item["quantity"] = quantity
                    break
        store_cart_cookie["cart_items"] = store_cart_items
        response = HttpResponseRedirect(reverse("cart"))
        if not cart_cookie_dict.get(store_name):
            cart_cookie_dict[store_name] = {}        
        cart_cookie_dict[store_name].update(store_cart_cookie)
        response.set_cookie('cart', value=json.dumps(cart_cookie_dict))
        
        return response

class DeleteCartItemView(BaseView):
    def post(self, request, store_name, variation_pk):
        cart_cookie = request.COOKIES.get("cart", "{}")
        cart_cookie_dict = json.loads(cart_cookie)
        store_cart_cookie = cart_cookie_dict.get(store_name, {})
        store_cart_items = store_cart_cookie.get("cart_items", [])

        if variation_pk == 'none':
            product_name = request.POST.get('name')
            store_cart_items = [item for item in store_cart_items if not (item["variation_id"] is None and item["name"] == product_name)]
        else:
            store_cart_items = [item for item in store_cart_items if item["variation_id"] != int(variation_pk)]

        store_cart_cookie["cart_items"] = store_cart_items

        response = HttpResponseRedirect(reverse("cart", kwargs={"store_name": store_name}))
        if not cart_cookie_dict.get(store_name):
            cart_cookie_dict[store_name] = {}        
        cart_cookie_dict[store_name].update(store_cart_cookie)
        response.set_cookie('cart', value=json.dumps(cart_cookie_dict))
        
        return response

class CheckoutView(BaseView):
    def get(self, request, store_name):
        cart_cookie = request.COOKIES.get("cart", "{}")
        cart_cookie_dict = json.loads(cart_cookie)
        store_cart_cookie = cart_cookie_dict.get(store_name, {})
        store_cart_items = []
        categories = Category.objects.all()
       
        try:
            account_info = request.user.account_info
        except AccountInfo.DoesNotExist:
            account_info = None

        shop = Shop.objects.filter(store_name=store_name).first()
        delivery_cost = shop.delivery_cost if shop else 0 

        for cart_item in store_cart_cookie.get("cart_items", []):
            if cart_item.get("variation_id"):
                temp_variation = ProductVariation.objects.filter(pk=cart_item.get("variation_id")).first()
                if not temp_variation:
                    continue
                store_cart_items.append(CartItem(
                    product_id=temp_variation.product.pk,
                    variation_id=temp_variation.pk,
                    price=cart_item.get("price"),
                    quantity=cart_item.get("quantity"),
                    name=cart_item.get("name"),
                    image=cart_item.get("image"),
                    color=temp_variation.color.color if temp_variation.color else None,
                    size=temp_variation.size,
                ))
            else:
                product = Product.objects.filter(name=cart_item.get("name")).first()
                if not product:
                    continue
                store_cart_items.append(CartItem(
                    product_id=product.pk,
                    variation_id=None,
                    price=cart_item.get("price"),
                    quantity=cart_item.get("quantity"),
                    name=cart_item.get("name"),
                    image=cart_item.get("image"),
                    color=None,
                    size=None,
                ))

        total_price = sum(item.price * item.quantity for item in store_cart_items)+ delivery_cost
        form = CheckoutForm()

        if not request.user.is_authenticated:
            messages.info(request, 'برای ادامه فرایند پرداخت باید وارد حساب کاربری خود شوید.') 
            return redirect('signin')
        
        if not account_info:
            messages.info(request, 'برای ادامه فرایند پرداخت باید حساب کاربری خود را تکمیل کنید.') 
            return redirect('account-info')
            
             
        return render(request, 'checkout.html', {
            'categories': categories,
            'cart_items': store_cart_items,
            'form': form,
            'total_price': total_price,
            'store_name': store_name,
             'delivery_cost':delivery_cost,
            'error_message': None  # Add this line
        })

    def post(self, request, store_name):
        categories = Category.objects.all()
        if not request.user.is_authenticated:
            return redirect('login')

        form = CheckoutForm(request.POST)
        if form.is_valid():
            cart_cookie = request.COOKIES.get("cart", "{}")
            cart_cookie_dict = json.loads(cart_cookie)
            store_cart_cookie = cart_cookie_dict.get(store_name, {})
            store_cart_items = store_cart_cookie.get("cart_items", [])
            
            shop = Shop.objects.filter(store_name=store_name).first()
            delivery_cost = shop.delivery_cost if shop else 0 

            total_price = sum(
                item.get("price") * item.get("quantity") for item in store_cart_cookie.get("cart_items", [])
            ) + delivery_cost 
            total_discount = sum(
                item.get("discount", 0.0) * item.get("quantity") for item in store_cart_cookie.get("cart_items", [])
            )

            # Check for item availability
            unavailable_items = []
            for cart_item in store_cart_cookie.get("cart_items", []):
                if cart_item.get("variation_id"):
                    temp_variation = ProductVariation.objects.filter(pk=cart_item.get("variation_id")).first()
                    if not temp_variation or temp_variation.quantity < cart_item.get("quantity"):
                        unavailable_items.append(cart_item.get("name"))
                else:
                    product = Product.objects.filter(name=cart_item.get("name")).first()
                    if not product:
                        continue
                    total_product_quantity = sum(variation.quantity for variation in product.variations.all())
                    if total_product_quantity < cart_item.get("quantity"):
                        unavailable_items.append(cart_item.get("name"))

            if unavailable_items:
                return render(request, 'checkout.html', {
                    'cart_items': store_cart_items,
                    'form': form,
                    'categories': categories,
                    'total_price': total_price,
                    'store_name': store_name,
                    'error_message': f"The following items are not available in the required quantity: {', '.join(unavailable_items)}"
                })

            order = Order.objects.create(
                account=request.user,
                total_price=total_price,
                total_discount=total_discount,
                delivery_address_unit_number=form.cleaned_data.get('delivery_address_unit_number', ''),
                delivery_address_street_name=form.cleaned_data.get('delivery_address_street_name', ''),
                delivery_address_suburb=form.cleaned_data.get('delivery_address_suburb', ''),
                delivery_address_city=form.cleaned_data.get('delivery_address_city', ''),
                delivery_address_state=form.cleaned_data.get('delivery_address_state', ''),
                delivery_address_postcode=form.cleaned_data.get('delivery_address_postcode', ''),
                shop=shop,
                
            )

            for cart_item in store_cart_cookie.get("cart_items", []):
                if cart_item.get("variation_id"):
                    temp_variation = ProductVariation.objects.filter(pk=cart_item.get("variation_id")).first()
                    if not temp_variation:
                        continue
                    OrderItem.objects.create(
                        variation=temp_variation,
                        variation_price=cart_item.get("price"),
                        order=order,
                        quantity=cart_item.get("quantity"),
                        total_price=cart_item.get("price") * cart_item.get("quantity"),
                        discount=cart_item.get("discount", 0.0),
                    )
                else:
                    product = Product.objects.filter(name=cart_item.get("name")).first()
                    if not product:
                        continue
                    OrderItem.objects.create(
                        variation=None,
                        variation_price=cart_item.get("price"),
                        order=order,
                        quantity=cart_item.get("quantity"),
                        total_price=cart_item.get("price") * cart_item.get("quantity"),
                        discount=cart_item.get("discount", 0.0),
                    )

            # Prepare the payment request to ZarinPal
            callback_url = request.build_absolute_uri(f'/callback/{quote(store_name)}/')
            req_data = {
                "merchant_id": settings.ZARINPAL_MERCHANT_ID,
                "amount": total_price*10,
                "callback_url": callback_url,
                "description": "Order #{}".format(order.id),
                "metadata": {"email": request.user.email}
            }
            req_header = {"accept": "application/json", "content-type": "application/json"}
            response = requests.post(url=settings.ZARINPAL_WEBSERVICE, json=req_data, headers=req_header)

            if response.status_code == 200:
                response_data = response.json()
                if response_data['data']['code'] == 100:
                    authority = response_data['data']['authority']
                    order.payment_authority = authority
                    order.save()
                    return redirect(f'https://www.zarinpal.com/pg/StartPay/{authority}')
                else:
                    return render(request, 'error.html', {'message': response_data['errors']})
            else:
                return render(request, 'error.html', {'message': 'An error occurred during the payment process.'})
        else:
            cart_cookie = request.COOKIES.get("cart", "{}")
            cart_cookie_dict = json.loads(cart_cookie)
            store_cart_cookie = cart_cookie_dict.get(store_name, {})
            store_cart_items = []


            for cart_item in store_cart_cookie.get("cart_items", []):
                if cart_item.get("variation_id"):
                    temp_variation = ProductVariation.objects.filter(pk=cart_item.get("variation_id")).first()
                    if not temp_variation:
                        continue
                    store_cart_items.append(CartItem(
                        product_id=temp_variation.product.pk,
                        variation_id=temp_variation.pk,
                        price=cart_item.get("price"),
                        quantity=cart_item.get("quantity"),
                        name=cart_item.get("name"),
                        image=cart_item.get("image"),
                        color=temp_variation.color.color,
                        size=temp_variation.size,
                    ))
                else:
                    product = Product.objects.filter(name=cart_item.get("name")).first()
                    if not product:
                        continue
                    store_cart_items.append(CartItem(
                        product_id=product.pk,
                        variation_id=None,
                        price=cart_item.get("price"),
                        quantity=cart_item.get("quantity"),
                        name=cart_item.get("name"),
                        image=cart_item.get("image"),
                        color=None,
                        size=None,
                    ))

            total_price = sum(item.price * item.quantity for item in store_cart_items)

            return render(request, 'checkout.html', {
                'cart_items': store_cart_items,
                'form': form,
                'total_price': total_price,
                'store_name': store_name,
                'categories': categories,
                'error_message': None , # Add this line
                'delivery_cost':delivery_cost
            })


class SuccessfulOrdr(BaseView) :
    
    def get(self, request): 
        orders = Order.objects.filter( account=request.user)
        return render(request,'successful_order.html',{'orders':orders})
     
class OrderListView(BaseView):
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        shop_instance = Shop.objects.filter(account=request.user)
        orders = Order.objects.filter( account=request.user,  is_paid=True)
        if self.request.htmx:
           return render(request, 'orders.html', {'orders': orders,'shop_instance': shop_instance})
        return render(request, 'orders_full.html', {'orders': orders, 'shop_instance': shop_instance})  
         
      


class OrderDetailView(BaseView):
    def get(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('login')
        try:    order = Order.objects.get(pk=pk, account=request.user)
        except Order.DoesNotExist:
            return redirect('orders')
        
        order_items = OrderItem.objects.filter(order=order)
       
        
        return render(request, 'orderdetails.html', {'order': order, 'order_items': order_items})
        
