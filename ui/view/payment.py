from django.shortcuts import render, redirect , get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect
import requests
from urllib.parse import quote, unquote
import json
from store.models import Order
from django.urls import reverse



from urllib.parse import quote, unquote
from store.models import Order

def zarinpal_callback(request, store_name):
    authority = request.GET.get('Authority')
    status = request.GET.get('Status')

    if status == 'OK':
        order = Order.objects.filter(payment_authority=authority).first()
        if not order:
            return render(request, 'error.html', {'message': 'Order not found.'})

        req_data = {
            "merchant_id": settings.ZARINPAL_MERCHANT_ID,
            "authority": authority,
            "amount": order.total_price
        }
        req_header = {"accept": "application/json", "content-type": "application/json"}
        response = requests.post(url=settings.ZARINPAL_PAYMENT_VERIFICATION, json=req_data, headers=req_header)

        if response.status_code == 200:
            response_data = response.json()
            if response_data['data']['code'] == 100:
                order.is_paid = True
                order.save()

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
        total_price = order.total_price

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
