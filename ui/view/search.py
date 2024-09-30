from django.db.models import Q
from django.shortcuts import render
from store.models import Product, Shop
from utils.views import BaseView

class Search_view(BaseView):
     def get(self, request):
        query = request.GET.get('q')
        if query:
            product_results = Product.objects.filter(name__icontains=query, is_approved=True)
            shop_results = Shop.objects.filter(store_name__icontains=query, is_approved=True)
          
            return render(request, 'searchresults.html', {'query': query, 'product_results': product_results, 'shop_results': shop_results})
        else:
            return render(request, 'searchresults.html', {'query': query, 'product_results': None, 'shop_results': None})
