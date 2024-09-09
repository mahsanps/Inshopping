from django.shortcuts import render, redirect, get_object_or_404
from utils.views import BaseView
from store.models import Shop, OrderItem, Product, Order
from datetime import datetime, timedelta
from django.db.models import Sum, F
from django.utils.timezone import make_aware
from django.db.models import Q
from django.http import JsonResponse
from store.choices import OrderStatusChoices
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from utils.views import BaseView
from store.models import Shop, OrderItem, Product, OrderDelivery
from datetime import datetime, timedelta
from django.db.models import Sum, F
from django.utils.timezone import make_aware
from ui.forms.orderdelivery import OrderDeliveryForm


class Dashboard(BaseView):
    def get(self, request, *args, **kwargs):
        shop = request.user.shop_set.first()
        shop_instance = Shop.objects.filter(account=request.user)
        
        # Filter order items related to paid orders
        order_items = OrderItem.objects.filter(variation__product__shop=shop, order__is_paid=True)
        
        # Orders that are paid and registered
        orders_registered = Order.objects.filter(id__in=order_items.values('order_id'), is_paid=True).distinct().select_related('delivery')
        
        # Correct calculation for total price
        total_price = sum(item.variation.product.price * item.quantity for item in order_items)

        now = datetime.now()

        # Daily sales
        start_of_today = make_aware(datetime.combine(now.date(), datetime.min.time()))
        end_of_today = make_aware(datetime.combine(now.date(), datetime.max.time()))
        daily_sales = order_items.filter(order__created_at__range=(start_of_today, end_of_today)).aggregate(
            total=Sum(F('variation__product__price') * F('quantity'))
        )['total'] or 0

        # Weekly sales (last 7 days)
        start_of_week = make_aware(now - timedelta(days=now.weekday()))
        weekly_sales = order_items.filter(order__created_at__gte=start_of_week).aggregate(
            total=Sum(F('variation__product__price') * F('quantity'))
        )['total'] or 0

        # Monthly sales (current month)
        start_of_month = make_aware(datetime(now.year, now.month, 1))
        monthly_sales = order_items.filter(order__created_at__gte=start_of_month).aggregate(
            total=Sum(F('variation__product__price') * F('quantity'))
        )['total'] or 0

        # Get top sold products
        daily_top_products = self.get_top_sold_products(shop, 'daily')
        weekly_top_products = self.get_top_sold_products(shop, 'weekly')
        monthly_top_products = self.get_top_sold_products(shop, 'monthly')

        context = {
            'orders_registered': orders_registered,
            'total_price': total_price,
            'daily_sales': daily_sales,
            'weekly_sales': weekly_sales,
            'monthly_sales': monthly_sales,
            'daily_top_products': daily_top_products,
            'weekly_top_products': weekly_top_products,
            'monthly_top_products': monthly_top_products,
            'shop_instance': shop_instance,
        }
        
        if self.request.htmx:
            return render(request, 'dashboard.html', context)
        return render(request, 'dashboard_full.html', context)
    
    def get_top_sold_products(self, shop, period):
        now = datetime.now()

        if period == 'daily':
            start_time = make_aware(datetime.combine(now.date(), datetime.min.time()))
            end_time = make_aware(datetime.combine(now.date(), datetime.max.time()))
        elif period == 'weekly':
            start_time = make_aware(now - timedelta(days=now.weekday()))
            end_time = make_aware(datetime.combine(now.date(), datetime.max.time()))
        elif period == 'monthly':
            start_time = make_aware(datetime(now.year, now.month, 1))
            end_time = make_aware(datetime.combine(now.date(), datetime.max.time()))
        else:
            raise ValueError("Invalid period. Choose 'daily', 'weekly', or 'monthly'.")

        # Filter top products based on paid orders within the specified time range
        top_products = Product.objects.filter(
            shop=shop,
            variations__order_items__order__is_paid=True,
            variations__order_items__order__created_at__range=(start_time, end_time)
        ).annotate(
            total_sold=Sum(F("variations__order_items__quantity"))
        ).order_by("-total_sold")[:5]

        return top_products

  
        
class ShopOrdersView(BaseView):
    def get(self, request, *args, **kwargs):
        shop = request.user.shop_set.first()
        order_pk = kwargs['pk']
        orders_registered=OrderItem.objects.filter(variation__product__shop=shop,  order_id=order_pk) 
        return render(request,'order-registered-details.html',{"orders_registered":orders_registered})  
    
    

class OrderDeliveryView(BaseView):
    def get(self, request, *args, **kwargs):
        order_id = kwargs.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        
        order_delivery, created = OrderDelivery.objects.get_or_create(order=order)
        
        form = OrderDeliveryForm(instance=order_delivery)
        return render(request, 'order-delivery.html', {'form': form, 'order_id': order_id})

    def post(self, request, *args, **kwargs):
        order_id = kwargs.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        
        order_delivery, created = OrderDelivery.objects.get_or_create(order=order)
        
        form = OrderDeliveryForm(request.POST, instance=order_delivery)
        
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to a success page or another page

        return render(request, 'order-delivery.html', {'form': form, 'order_id': order_id})
