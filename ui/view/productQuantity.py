from django.shortcuts import render, redirect, get_object_or_404
from store.models import  Color, Product, ProductVariation, Shop
from ui.forms.productQuantity import ProductsQuantityForm
from utils.views import BaseView




class ProductQuantityView(BaseView):
    def get(self, request, product_pk, *args, **kwargs,):
        product = get_object_or_404(Product, pk=product_pk)
    
        color = Color.objects.all()
        initial = {"product_id": product.pk}
        form = ProductsQuantityForm(initial=initial)
        return render(request, 'productsquantity.html', {'form': form, 'color': color, "product": product})

    def post(self, request, product_pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_pk)
       
        
        color = Color.objects.all()
        data = request.POST
        submit = data.get("continue")
        addmore = data.get("addmore")
        colors_data = data.getlist('color') 
        
        color_instance = None  
        if colors_data:
            try:
                color_instance = Color.objects.get(pk=colors_data[0])  #
            except Color.DoesNotExist:
                color_instance = None 
    
        form = ProductsQuantityForm(data)
        if form.is_valid():
            quantity = form.save(commit=False)
            quantity.product = product  
            quantity.color = color_instance 
            
            product.is_ready = True
            product.save()

            # Save the quantity
            quantity.save()

            if addmore == "True":
                form = ProductsQuantityForm()
                return render(request, 'productsquantity.html', {'form': form, "product": product, 'color': color})
            else:
                quantity.save()
                return redirect('product_details', product_pk=product_pk)

        return render(request, 'productsquantity.html', {'form': form, 'color': color, "product": product, 'color_instance': color_instance})

            
       


class ProductQuantityLists(BaseView):
    def get(self, request, *args, **kwargs):
        previous_form = ProductQuantityView.objects.all()
        return render(request, 'productquantitylists.html', {'previous_form': previous_form})





class EditProductVariation(BaseView):
    def get(self, request, product_pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_pk)
        variations = ProductVariation.objects.filter(product=product)
        variation_forms = []
        for variation in variations:
            variation_forms.append(ProductsQuantityForm(instance=variation))
        shop_instance = Shop.objects.filter(account=request.user).first()
        if self.request.htmx:    
          return render(request, 'productedit.html', {'shop_instance':shop_instance,'variation_forms': variation_forms, 'product': product})
        return render(request, 'productedit-full.html', {'shop_instance':shop_instance,'variation_forms': variation_forms, 'product': product})
    
    def post(self, request, product_pk, *args, **kwargs): 
        product = get_object_or_404(Product, pk=product_pk) 
        action = request.POST.get('action')
        variation_form = None  # Initialize variation_form here
        
        if action == 'save':
            variation_id = request.POST.get('variation_id')
            if variation_id:
                variation_obj = get_object_or_404(ProductVariation, pk=variation_id)
                variation_form = ProductsQuantityForm(request.POST, instance=variation_obj)
                
            else:
                variation_form = ProductsQuantityForm(request.POST)

            if variation_form.is_valid():
               variation_form.save()
                
        elif action == 'delete':
            variation_id = request.POST.get('variation_id')
            if variation_id:
                variation_obj = get_object_or_404(ProductVariation, pk=variation_id)
                variation_obj.delete()

        variations = ProductVariation.objects.filter(product=product)
        variation_forms = []
        for variation in variations:
            variation_forms.append(ProductsQuantityForm(instance=variation))

        return render(request, 'productedit.html', {'variation_forms': variation_forms, 'product': product})
