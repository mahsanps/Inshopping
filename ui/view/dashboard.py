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

from ui.forms.orderdelivery import OrderDeliveryForm
import json
import jdatetime
from datetime import datetime, timedelta

from django.utils.timezone import now as django_now  # Use Django's timezone-aware `now`

from django.utils.timezone import make_aware, is_naive


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

        # Use timezone-aware `now` from Django
        now = django_now()

        # Daily sales
        start_of_today = datetime.combine(now.date(), datetime.min.time())
        end_of_today = datetime.combine(now.date(), datetime.max.time())

        # Ensure the datetime is naive before making it timezone-aware
        if is_naive(start_of_today):
            start_of_today = make_aware(start_of_today)
        if is_naive(end_of_today):
            end_of_today = make_aware(end_of_today)

        daily_sales = OrderItem.objects.filter(
            variation__product__shop=shop,
            order__is_paid=True,
            order__created_at__range=(start_of_today, end_of_today)
        ).aggregate(total=Sum(F('variation__product__price') * F('quantity')))['total'] or 0

        # Weekly sales (last 7 days)
        start_of_week = now - timedelta(days=now.weekday())
        if is_naive(start_of_week):
            start_of_week = make_aware(start_of_week)

        weekly_sales = order_items.filter(order__created_at__gte=start_of_week).aggregate(
            total=Sum(F('variation__product__price') * F('quantity'))
        )['total'] or 0

        # Monthly sales (current month)
        start_of_month = datetime(now.year, now.month, 1)
        if is_naive(start_of_month):
            start_of_month = make_aware(start_of_month)

        monthly_sales = order_items.filter(order__created_at__gte=start_of_month).aggregate(
            total=Sum(F('variation__product__price') * F('quantity'))
        )['total'] or 0

        # Sales for the last 7 days
        last_7_days_sales = []
        last_7_days_labels = []
        for i in range(7):
            day = now - timedelta(days=i)

            # Start and end of the day
            start_of_day = datetime.combine(day.date(), datetime.min.time())
            end_of_day = datetime.combine(day.date(), datetime.max.time())

            if is_naive(start_of_day):
                start_of_day = make_aware(start_of_day)
            if is_naive(end_of_day):
                end_of_day = make_aware(end_of_day)

            # Calculate sales for each day
            daily_sales_for_day = OrderItem.objects.filter(
                variation__product__shop=shop,
                order__is_paid=True,
                order__created_at__range=(start_of_day, end_of_day)
            ).aggregate(total=Sum(F('variation__product__price') * F('quantity')))['total'] or 0

            # Convert Gregorian date to Jalali
            jalali_day = jdatetime.datetime.fromgregorian(datetime=day)

            last_7_days_sales.append(daily_sales_for_day)
            last_7_days_labels.append(jalali_day.strftime('%Y/%m/%d'))

        # Reverse the data so the oldest day comes first
        last_7_days_sales.reverse()
        last_7_days_labels.reverse()

        # Today's and yesterday's sales comparison
        start_of_yesterday = datetime.combine((now - timedelta(days=1)).date(), datetime.min.time())
        end_of_yesterday = datetime.combine((now - timedelta(days=1)).date(), datetime.max.time())

        if is_naive(start_of_yesterday):
            start_of_yesterday = make_aware(start_of_yesterday)
        if is_naive(end_of_yesterday):
            end_of_yesterday = make_aware(end_of_yesterday)

        today_sales = OrderItem.objects.filter(
            variation__product__shop=shop,
            order__is_paid=True,
            order__created_at__range=(start_of_today, now)
        ).aggregate(total=Sum(F('variation__product__price') * F('quantity')))['total'] or 0

        yesterday_sales = OrderItem.objects.filter(
            variation__product__shop=shop,
            order__is_paid=True,
            order__created_at__range=(start_of_yesterday, end_of_yesterday)
        ).aggregate(total=Sum(F('variation__product__price') * F('quantity')))['total'] or 0

        # Calculate sales comparison for the week
        start_of_this_week = now - timedelta(days=now.weekday())
        if is_naive(start_of_this_week):
            start_of_this_week = make_aware(start_of_this_week)

        start_of_last_week = now - timedelta(days=now.weekday() + 7)
        if is_naive(start_of_last_week):
            start_of_last_week = make_aware(start_of_last_week)

        end_of_last_week = start_of_this_week

        this_week_sales = OrderItem.objects.filter(
            variation__product__shop=shop,
            order__is_paid=True,
            order__created_at__gte=start_of_this_week
        ).aggregate(total=Sum(F('variation__product__price') * F('quantity')))['total'] or 0

        last_week_sales = OrderItem.objects.filter(
            variation__product__shop=shop,
            order__is_paid=True,
            order__created_at__range=(start_of_last_week, end_of_last_week)
        ).aggregate(total=Sum(F('variation__product__price') * F('quantity')))['total'] or 0

        # Get top sold products
        daily_top_products = self.get_top_sold_products(shop, 'daily')
        weekly_top_products = self.get_top_sold_products(shop, 'weekly')
        monthly_top_products = self.get_top_sold_products(shop, 'monthly')

        context = {
            'orders_registered': orders_registered,
            'total_price': total_price,
            'daily_sales': daily_sales,
            'last_7_days_sales': json.dumps(last_7_days_sales),
            'last_7_days_labels': json.dumps(last_7_days_labels),
            'weekly_sales': weekly_sales,
            'monthly_sales': monthly_sales,
            'daily_top_products': daily_top_products,
            'weekly_top_products': weekly_top_products,
            'monthly_top_products': monthly_top_products,
            'shop_instance': shop_instance,
            'today_sales': today_sales,
            'yesterday_sales': yesterday_sales,
            'this_week_sales': this_week_sales,
            'last_week_sales': last_week_sales,
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
