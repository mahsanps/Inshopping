from store.models import Product, SubCategory
from django.shortcuts import render, redirect
from django import forms
from dal import autocomplete



class ProductsForm(forms.ModelForm):
    subcategory = forms.ModelChoiceField(queryset=SubCategory.objects.all(), required=True)

    class Meta:
        model = Product
        fields = ('name', 'productCode', 'description', 'image', 'material', 'madeIn', 'price', 'category', 'subcategory')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(categoryname_id=category_id).order_by('subname')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set.order_by('subname')
            
        super(ProductsForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True   
        self.fields['productCode'].required = False 
        self.fields['description'].required = False 
        self.fields['image'].required = True 
        self.fields['material'].required = False 
        self.fields['madeIn'].required = False 
        self.fields['price'].required = True 
        self.fields['category'].required = True 
        self.fields['subcategory'].required = True  