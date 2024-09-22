from django.shortcuts import render, redirect , get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect
import requests
from urllib.parse import quote, unquote
import json
from store.models import Shop
from store.models import Order
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from urllib.parse import quote, unquote
from store.models import Order
from django.utils.html import format_html
from django.templatetags.static import static 
from django.contrib.sites.shortcuts import get_current_site


def send_order_notification_email( shop_email, order_id, store_name):
    subject = f" سفارش جدید فروشگاه {store_name} "
    from_email = settings.DEFAULT_FROM_EMAIL
   
    
    # HTML message with RTL and additional content
    html_message = format_html(
        """
        <div style="direction: rtl; text-align: right; font-family: Tahoma, sans-serif;">
           
            <p>فروشنده عزیز</p>
            <p>شما یک سفارش جدید با شماره سفارش: <strong>{order_id}</strong> دارید.</p>
            <p>لطفا پنل ادمین این شاپینگ خود را برای جزئیات سفارش ثبت شده مشاهده کنید.</p>
            <p>برای مشاهده سفارشات خود به <a href="{website_url}" style="color: #1a73e8; text-decoration: none;">این لینک</a> مراجعه کنید.</p>
            <p>با تشکر،</p>
            <p>تیم پشتیبانی این شاپینگ</p>
        </div>
        """,
  
        order_id=order_id,
        website_url="https://www.inshopping.ir/dashboard"  # Your actual admin orders URL
    )

    # Send the email
    send_mail(
        subject,
        '',  # Plain text version can be left empty if you are primarily sending HTML content
        from_email,
        [shop_email],
        fail_silently=False,
        html_message=html_message  # Set the HTML content
    )
    
def send_user_order_confirmation_email( user_email, order_id, store_name, first_name):
    subject = f" ثبت سفارش شما در فروشگاه {store_name} "
    from_email = settings.DEFAULT_FROM_EMAIL
    
    
    # HTML message with RTL and additional content
    html_message = format_html(
        """
        <div style="direction: rtl; text-align: right; font-family: Tahoma, sans-serif;">
            
            <p>{first_name} عزیز</p>
            <p>سفارش شما با شماره <strong>{order_id}</strong> با موفقیت ثبت شده است.</p>
            <p>شما می‌توانید برای مشاهده جزئیات سفارش خود به حساب کاربری‌تان در <a href="{website_url}" style="color: #1a73e8; text-decoration: none;">این شاپینگ</a> مراجعه کنید.</p>
            <p>با تشکر،</p>
            <p>تیم پشتیبانی این شاپینگ</p>
        </div>
        """,
     
        order_id=order_id,
        first_name=first_name,
        website_url="https://www.inshopping.ir/orders"  # Your actual user's order URL
    )

    # Send the email
    send_mail(
        subject,
        '',  # Plain text version can be left empty if you are primarily sending HTML content
        from_email,
        [user_email],
        fail_silently=False,
        html_message=html_message  # Set the HTML content
    )
    
    


def zarinpal_callback(request, store_name):
    authority = request.GET.get('Authority')
    status = request.GET.get('Status')

    if status == 'OK':
        order = Order.objects.filter(payment_authority=authority).first()
        if not order:
            return render(request, 'error.html', {'message': 'Order not found.'})
        
        price=order.total_price*10
        
        req_data = {
            "merchant_id": settings.ZARINPAL_MERCHANT_ID,
            "authority": authority,
            "amount": price
        }
        req_header = {"accept": "application/json", "content-type": "application/json"}
        response = requests.post(url=settings.ZARINPAL_PAYMENT_VERIFICATION, json=req_data, headers=req_header)

        if response.status_code == 200:
            response_data = response.json()
            if response_data['data']['code'] == 100:
                order.is_paid = True
                order.save()
                
                shop = Shop.objects.filter(store_name=store_name).first()
            if shop:
                # Include the request argument
                send_order_notification_email(shop.email, order.id, store_name)

            if order.account and order.account.email:
                first_name = order.account.account_info.firstname if order.account.account_info else "کاربر"
                # Include the request argument
                send_user_order_confirmation_email(order.account.email, order.id, store_name, first_name)

    


                # Clear the cart cookie and redirect to success page with store_name and authority
                success_url = f"/success/?ref_id={authority}&store_name={quote(store_name)}"
                response = HttpResponseRedirect(success_url)
                response.delete_cookie('cart')

                return response
            else:
                return render(request, 'error.html', {'message': response_data['errors']})
        else:
            return render(request, 'error.html', {'message': 'An error occurred during the payment verification process.'})
    else:
        return render(request, 'error.html', {'message': 'Payment was not successful.'})

def success_view(request):
    ref_id = request.GET.get('ref_id')
    store_name = unquote(request.GET.get('store_name')) if request.GET.get('store_name') else ''
    return render(request, 'success.html', {'ref_id': ref_id, 'store_name': store_name})


def initiate_payment(request, store_name, order_id):
    try:
        order = get_object_or_404(Order, id=order_id)
        total_price = order.total_price*10

        # Prepare the payment request to ZarinPal
        callback_url = request.build_absolute_uri(reverse('zarinpal_callback', kwargs={'store_name': quote(store_name)}))
        req_data = {
            "merchant_id": settings.ZARINPAL_MERCHANT_ID,
            "amount": total_price,
            "callback_url": callback_url,
            "description": f"Order #{order.id}",
            "metadata": {
                "email": request.user.email,
                
            }
        }
        req_header = {"accept": "application/json", "content-type": "application/json"}
        response = requests.post(url=settings.ZARINPAL_PAYMENT_REQUEST, json=req_data, headers=req_header)

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
    except Order.DoesNotExist:
        return render(request, 'error.html', {'message': 'Order not found.'})
